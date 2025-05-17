from typing import List, Union
from fastapi import APIRouter, Query
from app.services.rapidapi_service import RapidAPIService
from app.models_vm.fund_family_item_vm import FundFamilyItemVM


router = APIRouter(prefix="/funds", tags=["Funds"])
rapidapi_service = RapidAPIService()


@router.get("/fund-families", response_model=Union[List[FundFamilyItemVM], dict])
async def get_fund_families(mutual_fund_family: str = Query(..., description="Name of the Mutual Fund Family")):
    return await rapidapi_service.fetch_fund_families(mutual_fund_family=mutual_fund_family)