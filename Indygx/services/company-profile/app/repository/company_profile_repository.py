from typing import Any
from sqlmodel import Session, select
from ..database import get_session
from ..models import CompanySecondary, DigitalPresenceBrand


class CompanyProfileRepository:

    @staticmethod
    def get_profile(company_id: int):
        with get_session() as session:
            secondary = session.get(CompanySecondary, company_id)
            digital = session.get(DigitalPresenceBrand, company_id)

            return {
                "company_id": company_id,
                "secondary": secondary,
                "digital_presence_brand": digital,
            }

    @staticmethod
    def upsert_secondary(
        company_id: int,
        data: dict[str, Any],
        session: Session
    ):
        data["company_id"] = company_id
        existing = session.get(CompanySecondary, company_id)

        if existing:
            for k, v in data.items():
                setattr(existing, k, v)
            session.add(existing)
            return existing

        obj = CompanySecondary(**data)
        session.add(obj)
        return obj

    @staticmethod
    def upsert_digital_presence(
        company_id: int,
        data: dict[str, Any],
        session: Session
    ):
        data["company_id"] = company_id
        existing = session.get(DigitalPresenceBrand, company_id)

        if existing:
            for k, v in data.items():
                setattr(existing, k, v)
            session.add(existing)
            return existing

        obj = DigitalPresenceBrand(**data)
        session.add(obj)
        return obj
