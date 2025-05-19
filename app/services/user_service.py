from typing import Dict, Optional
from sqlalchemy.orm import Session
from app.services.base import Base
from app.models_db.user_orm import UserORM
from app.utils.auth import create_access_token
from app.utils.app_consts import AppFields, Messages
from app.repository.user_repository import UserRepository
from app.models_vm.user_vm import UserCreateVM, UserLoginVM
from app.utils.security import hash_password, verify_password


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
        token = create_access_token({"sub": user_vm.email})
        return self.resp_builder.build_success_response(data={AppFields.EMAIL: user_email, AppFields.ACCESS_TOKEN: token})


    
    def __get_user_by_email(self, user_data: UserCreateVM, db: Session) -> Optional[UserORM]:
        if not user_data or not user_data.email or not db:
            return None
        
        return self.user_repo.get_user_by_email(user_email=user_data.email, db=db)        


    def login_user(self, parameters: Dict, db: Session) -> str:
        # Step 1: Validate payload using schema
        result, is_valid = self.validate_json_payload_schema(UserLoginVM, parameters)

        if not is_valid:
            return result
        
        user_vm: UserLoginVM = result

        # Step 2: Check if user exists
        existing_user = self.__get_user_by_email(user_vm, db)
        if not existing_user or not verify_password(user_vm.password, existing_user.hashed_password):
            return self.resp_builder.build_warn_response(msg=Messages.INVALID_CREDENTIALS)

        # Step 5: Return success response
        token = create_access_token({"sub": user_vm.email})
        return self.resp_builder.build_success_response(data={AppFields.EMAIL: user_vm.email, AppFields.ACCESS_TOKEN: token})
