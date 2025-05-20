import asyncio
import logging
from fastapi import FastAPI
from backend.app.db import get_db
from backend.app.utils.app_consts import Schedulers
from backend.app.services.rapidapi_service import RapidAPIService


logger = logging.getLogger(__name__)
app = FastAPI()



async def schedule_nav_fetch():
    service = RapidAPIService()
    while True:
        db = next(get_db())
        for mf_family in Schedulers.MUTUAL_FUND_FAMILIES:
            try:
                await service.fetch_and_cache_navs(db, mf_family)
            except Exception as e:
                logger.error(f"SCHEDULER ERROR: {e}")
        await asyncio.sleep(3600)