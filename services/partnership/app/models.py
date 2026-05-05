from sqlmodel import SQLModel, Field


class PartnershipsEcosystem(SQLModel, table=True):
    __tablename__ = "partnerships_ecosystem"

    company_id: int = Field(primary_key=True)
    corporate_partnership_programs: str | None
    university_academic_partnerships: str | None
    industry_associations_memberships: str | None
    strategic_partnerships: str | None
    rd_investment_percentage: str | None
    technology_partners: str | None
