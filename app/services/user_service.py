from typing import Dict, Optional
from sqlalchemy.orm import Session
from app.repository.user_repository import UserRepository
from app.services.base import Base
from app.models_db.user_orm import UserORM
from app.models_vm.user_vm import UserCreateVM, UserLoginVM
from app.utils.app_consts import Messages
from app.utils.security import hash_password, verify_password
from app.utils.jwt import create_access_token
from fastapi import HTTPException, status


class UserService(Base):
    def __init__(self):
        super().__init__()
        self.user_repo = UserRepository()

    def register_user(self, user_data: Dict, db: Session) -> str:
        # Step 1: Validate payload using schema
        result, is_valid = self.validate_json_payload_schema(UserCreateVM, user_data)
        if not is_valid:
            return result

        user_vm: UserCreateVM = result

        # Step 2: Check if user already exists
        existing_user = self.__get_user_by_email(user_vm, db)
        if existing_user:
            return self.resp_builder.build_warn_response(
                msg=f"{Messages.EMAIL_ALREADY_REGISTERED}{user_vm.email}"
            )

        # Step 3: Create new user
        new_user = UserORM(
            user_email=user_vm.email,
            hashed_password=hash_password(user_vm.password)
        )

        # Step 4: Save user to DB
        user_email = self.user_repo.save_user(db, new_user)

        # Step 5: Return success response
        return self.resp_builder.build_success_response(data={"email": user_email})

    
    def __get_user_by_email(self, user_data: UserCreateVM, db: Session) -> Optional[UserORM]:
        if not user_data or not user_data.email or not db:
            return None
        
        return self.user_repo.get_user_by_email(user_email=user_data.email, db=db)        


    def login_user(user_data: UserLoginVM, db: Session) -> str:
        user = db.query(UserORM).filter(UserORM.user_email == user_data.email).first()
        if not user or not verify_password(user_data.password, user.hashed_password):
            raise HTTPException(status_code=401, detail="Invalid credentials")

        return create_access_token({"sub": user.user_email})
