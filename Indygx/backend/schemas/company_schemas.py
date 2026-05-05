# schemas/company_schemas.py (create this file)
from pydantic import BaseModel

class CompanyListItem(BaseModel):
    company_id: int
    company_name: str