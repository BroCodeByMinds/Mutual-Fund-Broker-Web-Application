from typing import Optional
from pydantic import BaseModel, Field

class BuyRequest(BaseModel):
    scheme_code: int
    units: float = Field(..., gt=0)
    price_per_unit: Optional[float] = Field(None, gt=0)

class SellRequest(BaseModel):
    scheme_code: int
    units_to_sell: float = Field(..., gt=0)
    price_per_unit: float = Field(None, gt=0)
