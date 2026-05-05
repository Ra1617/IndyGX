from fastapi import APIRouter, HTTPException
from ..repository.financials_funding_repository import FinancialsFundingRepository
from ..schemas.financials_funding import (
    FinancialsFundingCreateUpdate,
    FinancialsFundingRead,
)

financials_funding_router = APIRouter()


@financials_funding_router.get("/{company_id}", response_model=FinancialsFundingRead)
def get_financials_funding(company_id: int):
    obj = FinancialsFundingRepository.get(company_id)
    if not obj:
        raise HTTPException(status_code=404, detail="Not found")
    return obj


@financials_funding_router.put("/{company_id}", response_model=FinancialsFundingRead)
def upsert_financials_funding(
    company_id: int,
    payload: FinancialsFundingCreateUpdate
):
    return FinancialsFundingRepository.upsert(
        company_id,
        payload.model_dump(exclude_unset=True)
    )


@financials_funding_router.delete("/{company_id}")
def delete_financials_funding(company_id: int):
    ok = FinancialsFundingRepository.delete(company_id)
    if not ok:
        raise HTTPException(status_code=404, detail="Not found")
    return {"deleted": True}
