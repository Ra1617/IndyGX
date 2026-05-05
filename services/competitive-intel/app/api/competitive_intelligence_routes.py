from fastapi import APIRouter
from ..schemas.competitive_intelligence import CompetitiveIntelligenceCreateUpdate
from ..repository.competitive_intelligence_repository import CompetitiveIntelligenceRepository
from ..database import get_session

router = APIRouter(
    prefix="/companies/{company_id}/competitive-intelligence",
    tags=["Competitive Intelligence"]
)


@router.get("/")
def get_competitive_intelligence(company_id: int):
    return CompetitiveIntelligenceRepository.get(company_id)


@router.put("/")
def upsert_competitive_intelligence(
    company_id: int,
    payload: CompetitiveIntelligenceCreateUpdate
):
    with get_session() as session:
        CompetitiveIntelligenceRepository.upsert(
            company_id,
            payload.dict(exclude_unset=True),
            session
        )
        session.commit()
