from datetime import datetime
from app.utils.app_consts import AppFields


class AppUtils:

    def format_date(self, date: datetime) -> str:
        return date.strftime(AppFields.DATE_FORMAT) if date else None
