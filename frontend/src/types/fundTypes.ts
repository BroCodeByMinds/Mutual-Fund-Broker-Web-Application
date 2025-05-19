export interface FundFamily {
    family_fund_id: number;
    family_fund_name: string;
    created_date: string;
    updated_date: string;
    created_by_user_name: string;
    updated_by_user_name: string;
    is_deleted: boolean;
  }
  
  export interface FundFamiliesResponse {
    status_code: number;
    message: string | null;
    data: FundFamily[];
  }
  
  export interface OpenEndedScheme {
    Scheme_Code: number;
    ISIN_Div_Payout_ISIN_Growth: string;
    ISIN_Div_Reinvestment: string;
    Scheme_Name: string;
    Net_Asset_Value: number;
    Date: string;
    Scheme_Type: string;
    Scheme_Category: string;
    Mutual_Fund_Family: string;
  }
  