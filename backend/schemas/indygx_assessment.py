from pydantic import BaseModel

class IndygxAssessmentBase(BaseModel):
    
    previous_interactions: str | None
    partnership_potential_rating: str | None
    collaboration_opportunity_score: str | None
    complementary_services_match_score: str | None

    

class IndygxAssessmentCreateUpdate(IndygxAssessmentBase):

    pass            
class IndygxAssessmentRead(IndygxAssessmentBase):

    company_id: int

    class Config:
        from_attributes = True    
