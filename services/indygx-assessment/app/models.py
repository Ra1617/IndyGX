from sqlmodel import SQLModel, Field


class IndygxAssessment(SQLModel, table=True):
    __tablename__ = "indygx_assessment"

    company_id: int = Field(primary_key=True)
    previous_interactions_with_indygx: str | None
    partnership_potential_rating: str | None
    collaboration_opportunity_score: str | None
    complementary_services_match_score: str | None
