from pydantic import BaseModel


class CompetitiveIntelligenceBase(BaseModel):
    competitors: str | None
    unique_differentiators: str | None
    competitive_advantages: str | None
    weakness_gaps_in_offering: str | None
    key_challenges_and_needs: str | None


class CompetitiveIntelligenceCreateUpdate(CompetitiveIntelligenceBase):
    pass
