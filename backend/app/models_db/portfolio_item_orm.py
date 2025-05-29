from sqlalchemy import Column, Integer, Float, ForeignKey, DateTime, Boolean
from sqlalchemy.orm import relationship
from app.db import Base
from app.utils.app_consts import DataBaseTables, DataBaseSchemas, AppFields, ForeignKeys
from sqlalchemy.sql import func

class PortfolioItemORM(Base):
    __tablename__ = DataBaseTables.PORTFOLIO_ITEMS
    __table_args__ = {AppFields.SCHEMA: DataBaseSchemas.PORTFOLIO}

    portfolio_item_id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, index=True)  # FK to your users table
    scheme_code = Column(Integer, ForeignKey(f'{DataBaseSchemas.MASTER}.{DataBaseTables.NavCacheORM}.{ForeignKeys.SCHEMA_CODE}'), index=True)
    units_owned = Column(Float, default=0.0)
    avg_buy_price = Column(Float, default=0.0)
    created_date = Column(DateTime(timezone=True), default=func.now())
    updated_date = Column(DateTime(timezone=True), default=func.now(), onupdate=func.now())
    is_deleted = Column(Boolean, default=False)

    scheme = relationship("NavCacheORM", lazy="joined")
