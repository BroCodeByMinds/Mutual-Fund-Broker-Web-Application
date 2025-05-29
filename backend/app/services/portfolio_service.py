from typing import Dict, Optional
from sqlalchemy.orm import Session
from app.services.base import Base
from app.utils.app_consts import Messages
from app.models_db.nav_cache_orm import NavCacheORM
from app.models_db.transaction_orm import TransactionORM
from app.models_db.portfolio_item_orm import PortfolioItemORM
from app.helper.enums.transaction_enums import TransactionType
from app.repository.nav_cache_repository import NavCacheRepository
from app.repository.transaction_repository import TransactionsRepository
from app.repository.fortfolio_item_repository import FortFolioItemRepository
from app.helper.models_vm.buy_sell_request_vm import BuyRequest, SellRequest


class PortfolioService(Base):
    def __init__(self):
        super().__init__()
        self.nav_cache_repo = NavCacheRepository()
        self.port_item_repo = FortFolioItemRepository()
        self.transaction_repo = TransactionsRepository()
        

    def buy_scheme(self, db: Session, user_id: int, buy_req: Dict):
        is_valid, result = self.validate_json_payload_schema(BuyRequest, buy_req)
        if not is_valid:
            return result

        buy_req: BuyRequest = result
        nav_cache_orm = self.__get_schema(scheme_code=buy_req.scheme_code, db=db)

        if not nav_cache_orm:
            return self.resp_builder.build_warn_response(msg=Messages.SCHEME_NOT_FOUND)

        price_per_unit = buy_req.price_per_unit or nav_cache_orm.nav
        units_to_buy = buy_req.units
        total_amount = units_to_buy * price_per_unit

        try:
            portfolio_item = self.__get_user_portfolio(db, user_id, buy_req.scheme_code)

            if not portfolio_item:
                portfolio_item = self.__create_new_portfolio_item(
                    user_id, buy_req.scheme_code, units_to_buy, price_per_unit
                )
                self.port_item_repo.add_to_db(db, portfolio_item)
            else:
                self.__recalculate_average_buy_price(portfolio_item, units_to_buy, price_per_unit)

            transaction = self.__add_transaction(db, portfolio_item, units_to_buy, price_per_unit, total_amount)
            self.transaction_repo.add_to_db(db, transaction)

            self.transaction_repo.commit_updates(db)
            portfolio_item: PortfolioItemORM = self.port_item_repo.refresh_db(db, portfolio_item)

            return {
                "scheme_code": portfolio_item.scheme_code,
                "units_owned": portfolio_item.units_owned,
                "avg_buy_price": portfolio_item.avg_buy_price
            }

        except Exception as e:
            db.rollback()
            return self.resp_builder.build_error_response(msg=Messages.PURCHASE_TRANSACTION_FAILED, data=str(e))

    
    def __create_new_portfolio_item(self, user_id: int, scheme_code: str, units: float, price_per_unit: float) -> PortfolioItemORM:
        return PortfolioItemORM(
            user_id=user_id,
            scheme_code=scheme_code,
            units_owned=units,
            avg_buy_price=price_per_unit
        )


    def __recalculate_average_buy_price(
            self, portfolio_item: PortfolioItemORM, units_to_add: float, price_per_unit: float) -> PortfolioItemORM:
        old_total = portfolio_item.units_owned * portfolio_item.avg_buy_price
        new_total = units_to_add * price_per_unit
        total_units = portfolio_item.units_owned + units_to_add

        portfolio_item.avg_buy_price = (old_total + new_total) / total_units
        portfolio_item.units_owned = total_units

        return portfolio_item
    
    def __add_transaction(
            self, db: Session, portfolio_item: PortfolioItemORM, units: float, price_per_unit: float, total_amount: float) -> TransactionORM:
        transaction = TransactionORM(
            portfolio_item=portfolio_item,
            transaction_type=TransactionType.BUY.value,
            units=units,
            price_per_unit=price_per_unit,
            total_amount=total_amount
        )
        self.transaction_repo.add_to_db(db, transaction)


    def __get_schema(self, scheme_code: str, db: Session) -> Optional[NavCacheORM]:
        if not scheme_code:
            return None

        return self.nav_cache_repo.get_open_ended_scheme_by_code(scheme_code=scheme_code, db=db)
        
        
    def __get_user_portfolio(self, db: Session, user_id: int, scheme_code: str) -> Optional[PortfolioItemORM]:
        if not db or not user_id or not scheme_code:
            return None

        return self.port_item_repo.get_user_portfolio(db=db, user_id=user_id, scheme_code=scheme_code)