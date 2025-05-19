from fastapi import FastAPI
from backend.app.controller import user_controller, fund_controller

app = FastAPI()

app.include_router(user_controller.router)
app.include_router(fund_controller.router)