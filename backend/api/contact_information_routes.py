from fastapi import APIRouter, HTTPException
from ..repository.contact_information_repository import ContactInformationRepository
from ..schemas.contact_information import (
    ContactInformationCreateUpdate,
    ContactInformationRead,
)

contact_information_router = APIRouter()


@contact_information_router.get("/{company_id}", response_model=ContactInformationRead)
def get_contact_information(company_id: int):
    obj = ContactInformationRepository.get(company_id)
    if not obj:
        raise HTTPException(status_code=404, detail="Not found")
    return obj


@contact_information_router.put("/{company_id}", response_model=ContactInformationRead)
def upsert_contact_information(
    company_id: int,
    payload: ContactInformationCreateUpdate
):
    return ContactInformationRepository.upsert(
        company_id,
        payload.model_dump(exclude_unset=True)
    )


@contact_information_router.delete("/{company_id}")
def delete_contact_information(company_id: int):
    ok = ContactInformationRepository.delete(company_id)
    if not ok:
        raise HTTPException(status_code=404, detail="Not found")
    return {"deleted": True}
