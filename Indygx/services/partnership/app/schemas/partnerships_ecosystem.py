from pydantic import BaseModel


class PartnershipsEcosystemBase(BaseModel):
    corporate_partnership_programs: str | None
    university_academic_partnerships: str | None
    industry_associations_memberships: str | None
    strategic_partnerships: str | None
    rd_investment_percentage: str | None
    technology_partners: str | None


class PartnershipsEcosystemCreateUpdate(PartnershipsEcosystemBase):
    pass
