from app.db import get_db
from typing import List, Union
from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends, Query
from app.services.rapidapi_service import RapidAPIService
from app.models_vm.fund_family_item_vm import FundFamilyItemVM


router = APIRouter(prefix="/funds", tags=["Funds"])
rapidapi_service = RapidAPIService()


@router.get("/open-ended", response_model=Union[List[FundFamilyItemVM], dict])
async def get_open_ended_schemes(mutual_fund_family: str = Query(..., description="Name of the Mutual Fund Family")):
    return await rapidapi_service.get_open_ended_schemes(mutual_fund_family=mutual_fund_family)


@router.post("/fund-families")
async def get_fund_families(db: Session = Depends(get_db)) -> dict:
    return rapidapi_service.fetch_fund_families(db=db)