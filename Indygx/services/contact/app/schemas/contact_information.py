from pydantic import BaseModel


class ContactInformationBase(BaseModel):
    contact_email: str | None
    phone_number: str | None
    primary_contact_person_name: str | None
    primary_contact_person_title: str | None
    primary_contact_person_email: str | None
    primary_contact_person_phone_number: str | None
    decision_maker_accessibility: str | None


class ContactInformationCreateUpdate(ContactInformationBase):
    pass
