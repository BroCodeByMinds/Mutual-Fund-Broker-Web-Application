import os
import httpx
import logging
from pytest import Session
from dotenv import load_dotenv
from backend.app.services.base import Base
from pydantic import ValidationError
from typing import Dict, List, Union
from backend.app.utils.app_consts import Messages, QueryParams
from backend.app.models_vm.fund_family_item_vm import FundFamilyItemVM
from backend.app.repository.family_fund_repository import FamilyFundRepository
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


    async def get_open_ended_schemes(self, mutual_fund_family: str) -> Union[List[FundFamilyItemVM], Dict[str, str]]:
        url = f"{self.base_url}/latest"
        params = {
            QueryParams.RTA_AGENT_CODE_KEY: QueryParams.RTA_AGENT_CODE_VALUE,
            QueryParams.MUTUAL_FUND_FAMILY_KEY: mutual_fund_family
        }

        async with httpx.AsyncClient() as client:
            try:
                response = await client.get(url, headers=self.headers, params=params)
                response.raise_for_status()
                data = response.json()
            except httpx.HTTPStatusError as e:
                if e.response.status_code == 429:
                    return {"error": Messages.RATE_LIMIT_ERROR_MSG}
                raise

        valid_items: List[FundFamilyItemVM] = []
        for item in data:
            try:
                valid_items.append(FundFamilyItemVM(**item))
            except ValidationError as e:
                logger.warning(f"{Messages.VALIDATION_ERROR_MSG}: {e}")

        return valid_items
    

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