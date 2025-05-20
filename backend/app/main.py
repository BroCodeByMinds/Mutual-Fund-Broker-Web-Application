import asyncio
import logging
from fastapi import FastAPI
from contextlib import asynccontextmanager
from fastapi.middleware.cors import CORSMiddleware
from app.utils.app_consts import Messages
from app.controller import user_controller, fund_controller
from app.schedulers.nav_scheduler import schedule_nav_fetch

app = FastAPI()
logger = logging.getLogger(__name__)


origins = ["http://localhost:3000"]


app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(user_controller.router)
app.include_router(fund_controller.router)


@asynccontextmanager
async def lifespan(app: FastAPI):
    # On startup:
    scheduler_task = asyncio.create_task(schedule_nav_fetch())
    logger.info(Messages.NAV_SCHEDULER_STARTED)

    yield  # Run app

    # On shutdown:
    scheduler_task.cancel()
    try:
        await scheduler_task
    except asyncio.CancelledError:
        logger.info(Messages.NAV_SCHEDULER_CANCELLED)

app.router.lifespan_context = lifespan
