from fastapi import APIRouter, HTTPException
from ..repository.parnetships_ecosystem_repository import PartnershipsEcosystemRepository
from ..schemas.partnerships_ecosystem import (
    PartnershipsEcosystemCreateUpdate,
    PartnershipsEcosystemRead,
)

partnerships_ecosystem_router = APIRouter()


@partnerships_ecosystem_router.get("/{company_id}", response_model=PartnershipsEcosystemRead)
def get_partnerships_ecosystem(company_id: int):
    obj = PartnershipsEcosystemRepository.get(company_id)
    if not obj:
        raise HTTPException(status_code=404, detail="Not found")
    return obj


@partnerships_ecosystem_router.put("/{company_id}", response_model=PartnershipsEcosystemRead)
def upsert_partnerships_ecosystem(
    company_id: int,
    payload: PartnershipsEcosystemCreateUpdate
):
    return PartnershipsEcosystemRepository.upsert(
        company_id,
        payload.model_dump(exclude_unset=True)
    )


@partnerships_ecosystem_router.delete("/{company_id}")
def delete_partnerships_ecosystem(company_id: int):
    ok = PartnershipsEcosystemRepository.delete(company_id)
    if not ok:
        raise HTTPException(status_code=404, detail="Not found")
    return {"deleted": True}
