from backend.app.db import get_db
from typing import List, Union
from sqlalchemy.orm import Session
from backend.app.utils.auth import get_current_user
from fastapi import APIRouter, Depends, Query
from backend.app.services.rapidapi_service import RapidAPIService
from backend.app.models_vm.fund_family_item_vm import FundFamilyItemVM


router = APIRouter(prefix="/funds", tags=["Funds"])
rapidapi_service = RapidAPIService()


@router.get("/open-ended", response_model=Union[List[FundFamilyItemVM], dict])
async def get_open_ended_schemes(mutual_fund_family: str = Query(...), user: dict = Depends(get_current_user)):
    return await rapidapi_service.get_open_ended_schemes(mutual_fund_family=mutual_fund_family)


@router.get("/fund-families")
async def get_fund_families(db: Session = Depends(get_db), user: dict = Depends(get_current_user)) -> dict:
    return rapidapi_service.fetch_fund_families(db=db)