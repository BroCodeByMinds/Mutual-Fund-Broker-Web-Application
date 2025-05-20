from typing import Optional, List
from pydantic import BaseModel, Field


class FundFamilyItemVM(BaseModel):
    Scheme_Code: int = Field(None)
    ISIN_Div_Payout_ISIN_Growth: Optional[str] = Field(None)
    ISIN_Div_Reinvestment: Optional[str] = Field(None)
    Scheme_Name: str = Field(None)
    Net_Asset_Value: float = Field(None)
    Date: str  = Field(None)
    Scheme_Type: str = Field(None)
    Scheme_Category: str = Field(None)
    Mutual_Fund_Family: str = Field(None)