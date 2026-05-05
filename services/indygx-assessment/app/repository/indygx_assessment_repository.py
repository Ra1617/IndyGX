from typing import Any
from sqlmodel import Session
from ..database import get_session
from ..models import IndygxAssessment


class IndygxAssessmentRepository:

    @staticmethod
    def get(company_id: int):
        with get_session() as session:
            return session.get(IndygxAssessment, company_id)

    @staticmethod
    def upsert(
        company_id: int,
        data: dict[str, Any],
        session: Session
    ):
        data["company_id"] = company_id
        existing = session.get(IndygxAssessment, company_id)

        if existing:
            for k, v in data.items():
                setattr(existing, k, v)
            session.add(existing)
            return existing

        obj = IndygxAssessment(**data)
        session.add(obj)
        return obj
