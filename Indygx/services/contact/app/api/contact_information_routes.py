from fastapi import APIRouter
from ..schemas.contact_information import ContactInformationCreateUpdate
from ..repository.contact_information_repository import ContactInformationRepository
from ..database import get_session

router = APIRouter(
    prefix="/companies/{company_id}/contacts",
    tags=["Contact & Engagement"]
)


@router.get("/")
def get_contact_information(company_id: int):
    return ContactInformationRepository.get(company_id)


@router.put("/")
def upsert_contact_information(
    company_id: int,
    payload: ContactInformationCreateUpdate
):
    with get_session() as session:
        ContactInformationRepository.upsert(
            company_id,
            payload.dict(exclude_unset=True),
            session
        )
        session.commit()
