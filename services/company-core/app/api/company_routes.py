from fastapi import APIRouter
from ..schemas.company_primary import CompanyPrimaryCreateUpdate
from ..repository.company_repository import CompanyRepository
from ..database import get_session

router = APIRouter(prefix="/companies", tags=["Company Core"])


@router.get("/{company_id}")
def get_company(company_id: int):
    return CompanyRepository.get_company_by_id(company_id)



@router.put("/{company_id}")
def update_company(company_id: int, payload: CompanyPrimaryCreateUpdate):
    with get_session() as session:
        CompanyRepository.upsert(company_id, payload.dict(exclude_unset=True), session)
        session.commit()