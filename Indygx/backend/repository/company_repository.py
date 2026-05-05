from sqlmodel import select
from sqlalchemy import func

from ..database import get_session
from ..models import (
    CompanyPrimary,
    CompanySecondary,
    CompetitiveIntelligence,
    ContactInformation,
    DigitalPresenceBrand,
    FinancialsFunding,
    IndygxAssessment,
    PartnershipsEcosystem,
)


class CompanyRepository:

    @staticmethod
    def list_companies(
        filters,
        page: int,
        page_size: int,
    ):
        with get_session() as session:
            query = select(CompanyPrimary)

            if filters.company_name:
                query = query.where(
                    CompanyPrimary.company_name.ilike(
                        f"%{filters.company_name}%"
                    )
                )

            if filters.industry_segment:
                query = query.where(
                    CompanyPrimary.industry_segment == filters.industry_segment
                )

            total = session.exec(
                select(func.count()).select_from(query.subquery())
            ).one()

            results = session.exec(
                query.offset((page - 1) * page_size).limit(page_size)
            ).all()

            return results, total

    @staticmethod
    def get_company_by_id(company_id: int):
        with get_session() as session:
            stmt = (
                select(CompanyPrimary)
                .where(CompanyPrimary.company_id == company_id)
            )
            return session.exec(stmt).first()

    @staticmethod
    def get_company_full_profile(company_id: int):
        with get_session() as session:
            stmt = (
                select(CompanyPrimary)
                .where(CompanyPrimary.company_id == company_id)
            )
            company = session.exec(stmt).first()

            if not company:
                return None

            # Force-load relationships
            _ = company.secondary
            _ = company.competitive_intelligence
            _ = company.contact_information
            _ = company.digital_presence_brand
            _ = company.financials_funding
            _ = company.indygx_assessment
            _ = company.partnerships_ecosystem

            return company