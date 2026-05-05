from fastapi import APIRouter
from ..schemas.indygx_assessment import IndygxAssessmentCreateUpdate
from ..repository.indygx_assessment_repository import IndygxAssessmentRepository
from ..database import get_session

router = APIRouter(
    prefix="/companies/{company_id}/indygx-assessment",
    tags=["IndyGX Assessment"]
)


@router.get("/")
def get_indygx_assessment(company_id: int):
    return IndygxAssessmentRepository.get(company_id)


@router.put("/")
def upsert_indygx_assessment(
    company_id: int,
    payload: IndygxAssessmentCreateUpdate
):
    with get_session() as session:
        IndygxAssessmentRepository.upsert(
            company_id,
            payload.dict(exclude_unset=True),
            session
        )
        session.commit()
