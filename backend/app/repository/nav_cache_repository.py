import logging
from typing import List, Optional
from sqlalchemy.orm import Session
from app.models_db.family_fund_orm import FamilyFundORM
from app.models_db.nav_cache_orm import NavCacheORM
from app.models_vm.fund_family_item_vm import FundFamilyItemVM


logger = logging.getLogger(__name__)


class NavCacheRepository:
    def __init__(self):
        super().__init__()

    def upsert_nav_caches(self, db: Session, items: List[FundFamilyItemVM]) -> None:
        for item in items:
            existing: Optional[NavCacheORM] = db.query(NavCacheORM).filter_by(scheme_code=item.Scheme_Code).first()

            if existing:
                # Update fields
                existing.scheme_name = item.Scheme_Name
                existing.mutual_fund_family = item.Mutual_Fund_Family
                existing.scheme_type = item.Scheme_Type
                existing.scheme_category = item.Scheme_Category
                existing.nav = item.Net_Asset_Value
                existing.nav_date = item.Date
            else:
                # Insert new record
                new_nav = NavCacheORM(
                    scheme_code=item.Scheme_Code,
                    scheme_name=item.Scheme_Name,
                    mutual_fund_family=item.Mutual_Fund_Family,
                    scheme_type=item.Scheme_Type,
                    scheme_category=item.Scheme_Category,
                    nav=item.Net_Asset_Value,
                    nav_date=item.Date
                )
                db.add(new_nav)

        try:
            db.commit()
        except Exception as e:
            db.rollback()
            logger.error(f"Error committing NAV records: {e}")


    def get_open_ended_schemes(self, db: Session, mutual_fund_family_id: int) -> List[NavCacheORM]:
        return (
            db.query(NavCacheORM)
            .join(
                FamilyFundORM,
                FamilyFundORM.family_fund_name == NavCacheORM.mutual_fund_family
            )
            .filter(FamilyFundORM.family_fund_id == mutual_fund_family_id)
            .all()
        )
