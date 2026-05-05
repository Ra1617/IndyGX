from fastapi import APIRouter
from ..schemas.company_secondary import CompanySecondaryCreateUpdate
from ..schemas.digital_presence_brand import DigitalPresenceBrandCreateUpdate
from ..repository.company_profile_repository import CompanyProfileRepository
from ..database import get_session

router = APIRouter(
    prefix="/companies/{company_id}/profile",
    tags=["Company Profile"]
)


@router.get("/")
def get_company_profile(company_id: int):
    return CompanyProfileRepository.get_profile(company_id)


@router.put("/secondary")
def upsert_company_secondary(
    company_id: int,
    payload: CompanySecondaryCreateUpdate
):
    with get_session() as session:
        CompanyProfileRepository.upsert_secondary(
            company_id,
            payload.dict(exclude_unset=True),
            session
        )
        session.commit()


@router.put("/digital-presence")
def upsert_digital_presence(
    company_id: int,
    payload: DigitalPresenceBrandCreateUpdate
):
    with get_session() as session:
        CompanyProfileRepository.upsert_digital_presence(
            company_id,
            payload.dict(exclude_unset=True),
            session
        )
        session.commit()
