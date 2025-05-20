import os
import httpx
import logging
from pytest import Session
from dotenv import load_dotenv
from pydantic import ValidationError
from typing import Dict, List, Union
from backend.app.services.base import Base
from backend.app.utils.app_utils import AppUtils
from backend.app.models_db.nav_cache_orm import NavCacheORM
from backend.app.utils.app_consts import Messages, QueryParams
from backend.app.models_vm.fund_family_item_vm import FundFamilyItemVM
from backend.app.repository.family_fund_repository import FamilyFundRepository
from backend.app.repository.nav_cache_repository import NavCacheRepository
from backend.app.models_vm.family_fund_response_vm import FamilyFundResponseVM


load_dotenv()
RAPIDAPI_EKY = os.getenv("RAPIDAPI_KEY")
API_HOST = os.getenv("API_HOST")
logger = logging.getLogger(__name__)


class RapidAPIService(Base):
    def __init__(self):
        super().__init__()
        self.api_key = RAPIDAPI_EKY
        self.api_host = API_HOST
        self.base_url = f"https://{self.api_host}"
        self.headers = {"X-RapidAPI-Key": self.api_key, "X-RapidAPI-Host": self.api_host}
        self.fund_repo = FamilyFundRepository()
        self.nav_cache_repo = NavCacheRepository()
        self.app_utils = AppUtils()
        

    async def fetch_and_cache_navs(self, db: Session, mutual_fund_family: str) -> None:
        url = f"{self.base_url}/latest"
        params = {
            QueryParams.RTA_AGENT_CODE_KEY: QueryParams.RTA_AGENT_CODE_VALUE,
            QueryParams.MUTUAL_FUND_FAMILY_KEY: mutual_fund_family
        }

        try:
            async with httpx.AsyncClient() as client:
                response = await client.get(url, headers=self.headers, params=params)
                response.raise_for_status()
                raw_data = response.json()
        except httpx.HTTPStatusError as e:
            logger.warning(f"HTTP error ({e.response.status_code}) while fetching NAVs for {mutual_fund_family}: {e}")
            return
        except Exception as e:
            logger.error(f"Unexpected error while fetching NAVs: {e}")
            return

        nav_items = []
        for item in raw_data:
            try:
                validated = FundFamilyItemVM(**item)
                nav_items.append(validated)
            except ValidationError as e:
                logger.warning(f"Skipping invalid NAV record: {e}")

        if not nav_items:
            logger.info(f"No valid NAVs fetched for {mutual_fund_family}")
            return

        self.nav_cache_repo.upsert_nav_caches(db, nav_items)
        logger.info(f"{len(nav_items)} NAV records processed for {mutual_fund_family}")

    

    def fetch_fund_families(self, db: Session) -> List[Dict]:
        orm_funds = self.fund_repo.get_family_funds(db=db)
        response_data = []
        if orm_funds is not None and len(orm_funds) > 0:
            for orm_fund in orm_funds:
                family_fund_data = FamilyFundResponseVM(
                    family_fund_id=orm_fund.family_fund_id,
                    family_fund_name=orm_fund.family_fund_name,
                    created_date=orm_fund.created_date,
                    updated_date=orm_fund.updated_date,
                    created_by_user_name=orm_fund.created_by_user_name,
                    updated_by_user_name=orm_fund.updated_by_user_name,
                    is_deleted=orm_fund.is_deleted,
                )
                response_data.append(family_fund_data.model_dump())
        return self.resp_builder.build_success_response(data=response_data)
    

    def get_open_ended_schemes(self, db: Session, mutual_fund_family_id: int):
        if not mutual_fund_family_id:
            return self.resp_builder.build_success_response(data=None)
        
        nav_cache_orms: List[NavCacheORM] = self.nav_cache_repo.get_open_ended_schemes(
            db, mutual_fund_family_id
        )

        if not nav_cache_orms:
            return self.resp_builder.build_success_response(data=None)

        result: List[dict] = [
            FundFamilyItemVM(
                Scheme_Code=nav.scheme_code,
                Scheme_Name=nav.scheme_name,
                Net_Asset_Value=nav.nav,
                Date=self.app_utils.format_date(nav.nav_date),
                Scheme_Type=nav.scheme_type,
                Scheme_Category=nav.scheme_category,
                Mutual_Fund_Family=nav.mutual_fund_family,
            ).model_dump()
            for nav in nav_cache_orms
        ]

        return self.resp_builder.build_success_response(result)