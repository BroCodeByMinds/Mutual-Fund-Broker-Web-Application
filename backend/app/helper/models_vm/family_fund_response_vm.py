from pydantic import BaseModel
from typing import List, Optional
from datetime import datetime

class FamilyFundResponseVM(BaseModel):
    family_fund_id: int
    family_fund_name: str
    created_date: Optional[datetime] = None
    updated_date: Optional[datetime] = None
    created_by_user_name: Optional[str] = None
    updated_by_user_name: Optional[str] = None
    is_deleted: Optional[bool] = False

    model_config = {
        "from_attributes": True,  # enable ORM parsing
    }