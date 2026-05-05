from typing import Any
from sqlmodel import Session
from ..database import get_session
from ..models import CompetitiveIntelligence


class CompetitiveIntelligenceRepository:

    @staticmethod
    def get(company_id: int):
        with get_session() as session:
            return session.get(CompetitiveIntelligence, company_id)

    @staticmethod
    def upsert(
        company_id: int,
        data: dict[str, Any],
        session: Session
    ):
        data["company_id"] = company_id
        existing = session.get(CompetitiveIntelligence, company_id)

        if existing:
            for k, v in data.items():
                setattr(existing, k, v)
            session.add(existing)
            return existing

        obj = CompetitiveIntelligence(**data)
        session.add(obj)
        return obj
