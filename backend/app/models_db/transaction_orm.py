from sqlalchemy import Boolean, Column, DateTime, Enum, Float, ForeignKey, Integer, String, func
from app.helper.enums.transaction_enums import TransactionType
from app.utils.app_consts import DataBaseTables, DataBaseSchemas, AppFields, ForeignKeys
from app.db import Base

class TransactionORM(Base):
    __tablename__ = DataBaseTables.TRANSACTIONS
    __table_args__ = {AppFields.SCHEMA: DataBaseSchemas.PORTFOLIO}

    id = Column(Integer, primary_key=True, index=True)
    portfolio_item_id = Column(Integer, ForeignKey(f'{DataBaseSchemas.MASTER}.{DataBaseTables.PORTFOLIO_ITEMS}.{ForeignKeys.PORTFOLIO_ITEM_ID}'), index=True)
    transaction_type = Column(Enum(TransactionType), nullable=False)
    units = Column(Float, nullable=False)
    price_per_unit = Column(Float, nullable=False)
    total_amount = Column(Float, nullable=False)
    created_date = Column(DateTime(timezone=True), default=func.now())