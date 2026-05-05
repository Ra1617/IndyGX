from pydantic import BaseModel

class FinancialsFundingBase(BaseModel):
   
    annual_revenues: str | None
    annual_profits: str | None
    company_valuation: str | None
    yoy_growth_rate: str | None
    profitability_status: str | None
    market_share: str | None
    key_investors_backers: str | None
    exit_history: str | None
    recent_funding_rounds: str | None
    total_capital_raised: str | None

   

class FinancialsFundingCreateUpdate(FinancialsFundingBase):

    pass        
class FinancialsFundingRead(FinancialsFundingBase):

    company_id: int

    class Config:
        from_attributes = True    