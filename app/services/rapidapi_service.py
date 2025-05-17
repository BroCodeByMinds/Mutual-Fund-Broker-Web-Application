import logging
import os
import httpx
from dotenv import load_dotenv
from app.services.base import Base
from pydantic import ValidationError
from typing import Dict, List, Optional, Union
from app.utils.app_consts import Messages, QueryParams
from app.models_vm.fund_family_item_vm import FundFamilyItemVM

load_dotenv()

RAPIDAPI_EKY = os.getenv("RAPIDAPI_KEY")
API_HOST = os.getenv("API_HOST")
logger = logging.getLogger(__name__)


class RapidAPIService(Base):
    def __init__(self):
        self.api_key = RAPIDAPI_EKY
        self.api_host = API_HOST
        self.base_url = f"https://{self.api_host}"
        self.headers = {"X-RapidAPI-Key": self.api_key, "X-RapidAPI-Host": self.api_host}


    async def fetch_fund_families(self, mutual_fund_family: str) -> Union[List[FundFamilyItemVM], Dict[str, str]]:
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