from sqlalchemy import Boolean, Column, DateTime, Integer, String, func
from app.utils.app_consts import DataBaseTables, DataBaseSchemas, AppFields
from app.db import Base


class FamilyFundORM(Base): 
    __tablename__ = DataBaseTables.FAMILY_FUND_ORM
    __table_args__ = {AppFields.SCHEMA: DataBaseSchemas.MASTER}

    family_fund_id = Column(Integer, primary_key=True, index=True)
    family_fund_name = Column(String, unique=True, index=True, nullable=False)
    created_date = Column(DateTime(timezone=True), default=func.now())
    updated_date = Column(DateTime(timezone=True), default=func.now(), onupdate=func.now())
    created_by_user_name = Column(String)
    updated_by_user_name = Column(String)
    is_deleted = Column(Boolean, default=False)