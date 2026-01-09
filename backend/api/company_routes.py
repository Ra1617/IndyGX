from fastapi import APIRouter, HTTPException
from backend.repository.company_repository import CompanyRepository

router = APIRouter()

@router.get("/")
def list_companies():
    """
    List all companies (id + name).
    """
    return CompanyRepository.list_companies()

@router.get("/{company_id}")
def get_company(company_id: str):
    """
    Get basic company info by ID.
    """
    company = CompanyRepository.get_company_by_id(company_id)

    if not company:
        raise HTTPException(status_code=404, detail="Company not found")

    return company

@router.get("/{company_id}/full-profile")
def get_company_full_profile(company_id: str):
    """
    Get full company aggregate (all 1–1 tables).
    """
    company = CompanyRepository.get_company_full_profile(company_id)

    if not company:
        raise HTTPException(status_code=404, detail="Company not found")

    return company
 