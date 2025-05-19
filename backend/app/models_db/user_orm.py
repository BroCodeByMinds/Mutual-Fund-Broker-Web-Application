# user.py
from sqlalchemy import Boolean, Column, DateTime, Integer, String, func
from backend.app.utils.app_consts import DataBaseTables, DataBaseSchemas, AppFields
from backend.app.db import Base

class UserORM(Base): 
    __tablename__ = DataBaseTables.USERS
    __table_args__ = {AppFields.SCHEMA: DataBaseSchemas.MASTER}

    user_id = Column(Integer, primary_key=True, index=True)
    user_email = Column(String, unique=True, index=True, nullable=False)
    hashed_password = Column(String, nullable=False)
    created_date = Column(DateTime(timezone=True), default=func.now())
    updated_date = Column(DateTime(timezone=True), default=func.now(), onupdate=func.now())
    created_by_user_name = Column(String)
    updated_by_user_name = Column(String)
    is_deleted = Column(Boolean, default=False)


