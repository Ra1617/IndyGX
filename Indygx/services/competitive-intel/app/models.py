from sqlmodel import SQLModel, Field


class CompetitiveIntelligence(SQLModel, table=True):
    __tablename__ = "competitive_intelligence"

    company_id: int = Field(primary_key=True)
    competitors: str | None
    unique_differentiators: str | None
    competitive_advantages: str | None
    weakness_gaps_in_offering: str | None
    key_challenges_and_needs: str | None
