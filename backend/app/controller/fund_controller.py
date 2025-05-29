from app.db import get_db
from typing import List, Union
from sqlalchemy.orm import Session
from app.helper.constants.mfb_constants import UserConstants
from app.helper.models_vm.buy_sell_request_vm import BuyRequest
from app.services.portfolio_service import PortfolioService
from app.utils.auth import get_current_user
from fastapi import APIRouter, Depends, Query
from app.services.rapidapi_service import RapidAPIService


router = APIRouter(prefix="/funds", tags=["Funds"])
rapidapi_service = RapidAPIService()
portfolio_service = PortfolioService()


@router.get("/open-ended")
async def get_open_ended_schemes(
    db: Session = Depends(get_db), mutual_fund_family_id: int = Query(...), user: dict = Depends(get_current_user)):
    return rapidapi_service.get_open_ended_schemes(db=db, mutual_fund_family_id=mutual_fund_family_id)


@router.get("/fund-families")
async def get_fund_families(db: Session = Depends(get_db), user: dict = Depends(get_current_user)) -> dict:
    return rapidapi_service.fetch_fund_families(db=db)

@router.post("/buy")
async def buy_fund(buy_req: BuyRequest, db: Session = Depends(get_db), user: dict = Depends(get_current_user)):
    return portfolio_service.buy_scheme(db, user[UserConstants.USER_ID], buy_req)