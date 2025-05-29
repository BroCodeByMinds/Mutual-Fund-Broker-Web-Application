from typing import List, Optional
from sqlalchemy.orm import Session
from app.models_db.family_fund_orm import FamilyFundORM
from app.models_db.transaction_orm import TransactionORM


class TransactionsRepository:
    def __init__(self):
        super().__init__()

    def commit_updates(self, db: Session) -> None:
        db.commit()

    def add_to_db(db: Session, transaction: TransactionORM):
        db.add(transaction)