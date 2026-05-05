from pydantic import BaseModel
from .company_primary import CompanyPrimaryRead
from .company_secondary import CompanySecondaryBase
from .competitive_intelligence import CompetitiveIntelligenceBase
from .contact_information import ContactInformationBase
from .digital_presence_brand import DigitalPresenceBrandBase
from .financials_funding import FinancialsFundingBase
from .indygx_assessment import IndygxAssessmentBase
from .partnerships_ecosystem import PartnershipsEcosystemBase



class CompanyListItem(BaseModel):
    company_id: int
    company_name: str


class CompanyFullProfile(CompanyPrimaryRead):
    secondary: CompanySecondaryBase | None
    competitive_intelligence: CompetitiveIntelligenceBase | None
    contact_information: ContactInformationBase | None
    digital_presence_brand: DigitalPresenceBrandBase | None
    financials_funding: FinancialsFundingBase | None
    indygx_assessment: IndygxAssessmentBase | None
    partnerships_ecosystem: PartnershipsEcosystemBase | None