import requests
from django.conf import settings

API_BASE = settings.API_BASE_URL


def get(endpoint, params=None, timeout=10):
    """Make a GET request to the FastAPI backend."""
    try:
        response = requests.get(f"{API_BASE}{endpoint}", params=params, timeout=timeout)
        response.raise_for_status()
        return response.json(), None
    except requests.exceptions.ConnectionError:
        return None, "Backend is offline. Please start the FastAPI server."
    except requests.exceptions.HTTPError as e:
        if e.response.status_code == 404:
            return None, "Resource not found."
        return None, f"API error: {e.response.status_code}"
    except Exception as e:
        return None, f"Unexpected error: {str(e)}"


def list_companies(page=1, page_size=20, **filters):
    params = {"page": page, "page_size": page_size}
    params.update({k: v for k, v in filters.items() if v})
    return get("/companies/", params=params)


def get_company_full_profile(company_id):
    return get(f"/companies/{company_id}/full-profile")


def get_competitive_intelligence(company_id):
    return get(f"/competitive-intelligence/{company_id}")


def get_financials_funding(company_id):
    return get(f"/financials-funding/{company_id}")


def get_contact_information(company_id):
    return get(f"/contact-information/{company_id}")


def get_digital_presence_brand(company_id):
    return get(f"/digital-presence-brand/{company_id}")


def get_partnerships_ecosystem(company_id):
    return get(f"/partnerships-ecosystem/{company_id}")


def get_indygx_assessment(company_id):
    return get(f"/indygx-assessment/{company_id}")
