
from sqlalchemy import Boolean, Column, Date, DateTime, Float, Integer, String, func
from app.utils.app_consts import DataBaseTables, DataBaseSchemas, AppFields
from app.db import Base
from app.models_db.portfolio_item_orm import PortfolioItemORM
from app.models_db.transaction_orm import TransactionORM


class NavCacheORM(Base): 
    __tablename__ = DataBaseTables.NAV_CACHE_ORM
    __table_args__ = {AppFields.SCHEMA: DataBaseSchemas.MASTER}

    scheme_code = Column(Integer, primary_key=True, index=True)
    scheme_name = Column(String, nullable=False)
    mutual_fund_family = Column(String)
    scheme_type = Column(String)
    scheme_category = Column(String)
    nav = Column(Float, nullable=False)
    nav_date = Column(Date, nullable=False)
    created_date = Column(DateTime(timezone=True), default=func.now())
    updated_date = Column(DateTime(timezone=True), default=func.now(), onupdate=func.now())