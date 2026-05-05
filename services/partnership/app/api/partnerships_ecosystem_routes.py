from fastapi import APIRouter
from ..schemas.partnerships_ecosystem import PartnershipsEcosystemCreateUpdate
from ..repository.partnerships_ecosystem_repository import PartnershipsEcosystemRepository
from ..database import get_session

router = APIRouter(
    prefix="/companies/{company_id}/partnerships",
    tags=["Partnership & Ecosystem"]
)


@router.get("/")
def get_partnerships(company_id: int):
    return PartnershipsEcosystemRepository.get(company_id)


@router.put("/")
def upsert_partnerships(
    company_id: int,
    payload: PartnershipsEcosystemCreateUpdate
):
    with get_session() as session:
        PartnershipsEcosystemRepository.upsert(
            company_id,
            payload.dict(exclude_unset=True),
            session
        )
        session.commit()
