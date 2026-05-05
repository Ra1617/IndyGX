from sqlmodel import SQLModel, Field


class ContactInformation(SQLModel, table=True):
    __tablename__ = "contact_information"

    company_id: int = Field(primary_key=True)
    contact_email: str | None
    phone_number: str | None
    primary_contact_person_name: str | None
    primary_contact_person_title: str | None
    primary_contact_person_email: str | None
    primary_contact_person_phone_number: str | None
    decision_maker_accessibility: str | None
