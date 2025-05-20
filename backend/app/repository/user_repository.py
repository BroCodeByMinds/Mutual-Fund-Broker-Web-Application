from typing import Optional
from app.models_db.user_orm import UserORM
from sqlalchemy.orm import Session


class UserRepository:
    def __init__(self):
        super().__init__()

    
    def get_user_by_email(self, user_email: str, db: Session) -> Optional[UserORM]:
        return (
            db.query(UserORM)
            .filter(
                UserORM.user_email == user_email,
                UserORM.is_deleted.isnot(True)
            )
            .first()
        )
    
    def save_user(self, db: Session, user: UserORM) -> str:
        db.add(user)
        db.commit()
        db.refresh(user)
        return user.user_email
    
    def get_user_by_email_and_password(self, user_email: str, password: str, db: Session) -> Optional[UserORM]:
        return (
            db.query(UserORM)
            .filter(
                UserORM.user_email == user_email,
                UserORM.is_deleted.isnot(True)
            )
            .first()
        )
