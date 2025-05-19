from fastapi import FastAPI
from backend.app.controller import user_controller, fund_controller
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI()

# Add CORS middleware here:
origins = [
    "http://localhost:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(user_controller.router)
app.include_router(fund_controller.router)