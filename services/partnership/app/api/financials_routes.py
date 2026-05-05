from fastapi import APIRouter
from ..schemas.partnerships_ecosystem import FinancialsFundingCreateUpdate
from ..repository.partnerships_ecosystem_repository import FinancialsRepository
from ..database import get_session

router = APIRouter(
    prefix="/companies/{company_id}/financials",
    tags=["Financial Intelligence"]
)


@router.get("/")
def get_financials(company_id: int):
    return FinancialsRepository.get_financials(company_id)


@router.put("/")
def upsert_financials(
    company_id: int,
    payload: FinancialsFundingCreateUpdate
):
    with get_session() as session:
        FinancialsRepository.upsert(
            company_id,
            payload.dict(exclude_unset=True),
            session
        )
        session.commit()
