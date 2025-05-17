from typing import Dict
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.db import get_db
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.db import get_db
from app.models_vm.user_vm import UserCreateVM, UserLoginVM, TokenVM
from app.services.user_service import UserService

router = APIRouter(prefix="/user", tags=["Auth"])
user_service = UserService()

@router.post("/register")
async def register(user: Dict, db: Session = Depends(get_db)) -> dict:
    return user_service.register_user(user_data=user, db=db)

    # async def login(self, user: UserLoginVM, db: Session = Depends(get_db)) -> dict:
    #     token = login_user(user, db)
    #     return {"access_token": token}
