from fastapi import APIRouter, HTTPException
from ..repository.digital_presence_brand_repository import DigitalPresenceBrandRepository
from ..schemas.digital_presence_brand import (
    DigitalPresenceBrandCreateUpdate,
    DigitalPresenceBrandRead,
)

digital_presence_brand_router = APIRouter()


@digital_presence_brand_router.get("/{company_id}", response_model=DigitalPresenceBrandRead)
def get_digital_presence_brand(company_id: int):
    obj = DigitalPresenceBrandRepository.get(company_id)
    if not obj:
        raise HTTPException(status_code=404, detail="Not found")
    return obj


@digital_presence_brand_router.put("/{company_id}", response_model=DigitalPresenceBrandRead)
def upsert_digital_presence_brand(
    company_id: int,
    payload: DigitalPresenceBrandCreateUpdate
):
    return DigitalPresenceBrandRepository.upsert(
        company_id,
        payload.model_dump(exclude_unset=True)
    )


@digital_presence_brand_router.delete("/{company_id}")
def delete_digital_presence_brand(company_id: int):
    ok = DigitalPresenceBrandRepository.delete(company_id)
    if not ok:
        raise HTTPException(status_code=404, detail="Not found")
    return {"deleted": True}
