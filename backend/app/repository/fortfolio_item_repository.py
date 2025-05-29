from typing import List, Optional
from sqlalchemy.orm import Session
from app.models_db.family_fund_orm import FamilyFundORM
from app.models_db.portfolio_item_orm import PortfolioItemORM
from app.models_db.user_orm import UserORM


class FortFolioItemRepository:
    def __init__(self):
        super().__init__()

    def get_user_portfolio(self, db: Session, user_id: int, scheme_code: str) -> List[PortfolioItemORM]:
        return (
            db.query(PortfolioItemORM)
            .filter(
                PortfolioItemORM.scheme_code == scheme_code,
                PortfolioItemORM.user_id == user_id,
                PortfolioItemORM.is_deleted.is_(False)
            )
            .all()
        )
    
    def refresh_db(self, db: Session, portfolio_item: PortfolioItemORM) -> PortfolioItemORM:
        db.refresh(portfolio_item)
        return portfolio_item
    
    def add_to_db(self, db: Session, portfolio_item: PortfolioItemORM):
        db.add(portfolio_item)
