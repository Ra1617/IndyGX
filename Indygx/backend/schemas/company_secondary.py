from pydantic import BaseModel, Field

class CompanySecondaryBase(BaseModel):


    
    twitter_handle: str | None
    facebook_page_url: str | None
    instagram_page_url: str | None
    key_business_leaders_name: str | None
    key_business_leaders_linkedin_url: str | None
    regulatory_licenses_certifications: str | None
    compliance_track_record: str | None
    legal_issues_controversies: str | None
    processing_time: str | None
    success_rate: str | None

    

class CompanySecondaryCreateUpdate(CompanySecondaryBase):

    pass
class CompanySecondaryRead(CompanySecondaryBase):

    company_id: int

    class Config:
        from_attributes = True