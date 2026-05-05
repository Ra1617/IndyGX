from fastapi import APIRouter, HTTPException
from ..repository.company_secondary_repository import CompanySecondaryRepository
from ..schemas.company_secondary import (
    CompanySecondaryCreateUpdate,
    CompanySecondaryRead,
)

router = APIRouter()

@router.get("/{company_id}", response_model=CompanySecondaryRead)
def get_secondary(company_id: int):
    obj = CompanySecondaryRepository.get(company_id)
    if not obj:
        raise HTTPException(status_code=404, detail="Not found")
    return obj

@router.put("/{company_id}", response_model=CompanySecondaryRead)
def upsert_secondary(
    company_id: int,
    payload: CompanySecondaryCreateUpdate
):
    return CompanySecondaryRepository.upsert(
        company_id,
        payload.model_dump(exclude_unset=True)
    )

@router.delete("/{company_id}")
def delete_secondary(company_id: int):
    ok = CompanySecondaryRepository.delete(company_id)
    if not ok:
        raise HTTPException(status_code=404, detail="Not found")
    return {"deleted": True}
 