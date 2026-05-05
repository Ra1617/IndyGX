from fastapi import APIRouter, HTTPException
from ..repository.competitive_intelligence_repository import CompetitiveIntelligenceRepository
from ..schemas.competitive_intelligence import (
    CompetitiveIntelligenceCreateUpdate,
    CompetitiveIntelligenceRead,
)

competitive_intelligence_router = APIRouter()


@competitive_intelligence_router.get("/{company_id}", response_model=CompetitiveIntelligenceRead)
def get_competitive_intelligence(company_id: int):
    obj = CompetitiveIntelligenceRepository.get(company_id)
    if not obj:
        raise HTTPException(status_code=404, detail="Not found")
    return obj


@competitive_intelligence_router.put("/{company_id}", response_model=CompetitiveIntelligenceRead)
def upsert_competitive_intelligence(
    company_id: int,
    payload: CompetitiveIntelligenceCreateUpdate
):
    return CompetitiveIntelligenceRepository.upsert(
        company_id,
        payload.model_dump(exclude_unset=True)
    )


@competitive_intelligence_router.delete("/{company_id}")
def delete_competitive_intelligence(company_id: int):
    ok = CompetitiveIntelligenceRepository.delete(company_id)
    if not ok:
        raise HTTPException(status_code=404, detail="Not found")
    return {"deleted": True}
