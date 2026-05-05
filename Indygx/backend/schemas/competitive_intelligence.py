from pydantic import BaseModel

class CompetitiveIntelligenceBase(BaseModel):
   
    competitors: str | None
    unique_differentiators: str | None
    competitive_advantages: str | None
    weakness_gaps: str | None
    key_challenges_needs: str | None

    
class CompetitiveIntelligenceCreateUpdate(CompetitiveIntelligenceBase):

    pass
class CompetitiveIntelligenceRead(CompetitiveIntelligenceBase):

    company_id: int

    class Config:
        from_attributes = True