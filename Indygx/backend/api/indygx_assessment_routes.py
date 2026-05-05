from fastapi import APIRouter, HTTPException
from ..repository.indygx_assessment_repository import IndygxAssessmentRepository
from ..schemas.indygx_assessment import (
    IndygxAssessmentCreateUpdate,
    IndygxAssessmentRead,
)

indygx_assessment_router = APIRouter()


@indygx_assessment_router.get("/{company_id}", response_model=IndygxAssessmentRead)
def get_indygx_assessment(company_id: int):
    obj = IndygxAssessmentRepository.get(company_id)
    if not obj:
        raise HTTPException(status_code=404, detail="Not found")
    return obj


@indygx_assessment_router.put("/{company_id}", response_model=IndygxAssessmentRead)
def upsert_indygx_assessment(
    company_id: int,
    payload: IndygxAssessmentCreateUpdate
):
    return IndygxAssessmentRepository.upsert(
        company_id,
        payload.model_dump(exclude_unset=True)
    )


@indygx_assessment_router.delete("/{company_id}")
def delete_indygx_assessment(company_id: int):
    ok = IndygxAssessmentRepository.delete(company_id)
    if not ok:
        raise HTTPException(status_code=404, detail="Not found")
    return {"deleted": True}
