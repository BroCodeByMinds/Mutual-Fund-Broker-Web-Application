from typing import List, Optional
from sqlalchemy.orm import Session
from backend.app.models_db.family_fund_orm import FamilyFundORM


class FamilyFundRepository:
    def __init__(self):
        super().__init__()

    def get_family_funds(self, db: Session) -> List[FamilyFundORM]:
        return (
            db.query(FamilyFundORM)
            .filter(
                FamilyFundORM.is_deleted.isnot(True)
            )
            .all()
        )