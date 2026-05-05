from pydantic import BaseModel


class IndygxAssessmentBase(BaseModel):
    previous_interactions_with_indygx: str | None
    partnership_potential_rating: str | None
    collaboration_opportunity_score: str | None
    complementary_services_match_score: str | None


class IndygxAssessmentCreateUpdate(IndygxAssessmentBase):
    pass
