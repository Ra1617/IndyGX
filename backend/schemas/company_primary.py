from pydantic import BaseModel

class CompanyPrimaryBase(BaseModel):
    type: str | None
    company_name: str | None
    year_of_incorporation: str | None
    industry_segment: str | None
    nature_of_company: str | None
    website_url: str | None
    linkedin_profile_url: str | None
    ceo_name: str | None
    ceo_linkedin_url: str | None
    employee_size: str | None
    services_offerings: str | None
    core_value_proposition: str | None
    focus_sectors_industries: str | None
    countries_operating_in: str | None
    geographic_coverage_india: str | None

class CompanyPrimaryCreateUpdate(CompanyPrimaryBase):
    pass

class CompanyPrimaryRead(CompanyPrimaryBase):
    company_id: int

    class Config:
        from_attributes = True
 