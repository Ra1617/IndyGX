from django.shortcuts import render, redirect
from django.contrib import messages
from . import api_client


def dashboard(request):
    """Main dashboard showing stats overview."""
    data, error = api_client.list_companies(page=1, page_size=100)
    stats = {
        'total_companies': 0,
        'recent_companies': [],
    }
    if data:
        stats['total_companies'] = data.get('meta', {}).get('total_records', 0)
        stats['recent_companies'] = data.get('data', [])[:6]

    return render(request, 'companies/dashboard.html', {
        'stats': stats,
        'error': error,
    })


def company_list(request):
    """Paginated company listing with filters."""
    page = int(request.GET.get('page', 1))
    page_size = 20
    search = request.GET.get('search', '')
    industry = request.GET.get('industry_segment', '')
    nature = request.GET.get('nature_of_company', '')

    data, error = api_client.list_companies(
        page=page,
        page_size=page_size,
        company_name=search,
        industry_segment=industry,
        nature_of_company=nature,
    )

    companies = []
    meta = {}
    if data:
        companies = data.get('data', [])
        meta = data.get('meta', {})

    # Build page range for pagination
    total_pages = meta.get('total_pages', 1)
    page_range = list(range(max(1, page - 2), min(total_pages + 1, page + 3)))

    return render(request, 'companies/company_list.html', {
        'companies': companies,
        'meta': meta,
        'page': page,
        'page_range': page_range,
        'search': search,
        'industry': industry,
        'nature': nature,
        'error': error,
    })


def company_detail(request, company_id):
    """Full company profile with all related data."""
    profile, error = api_client.get_company_full_profile(company_id)

    if error and not profile:
        return render(request, 'companies/error.html', {
            'error': error,
            'company_id': company_id,
        })

    return render(request, 'companies/company_detail.html', {
        'company': profile,
        'error': error,
        'active_tab': 'overview',
    })


def competitive_intelligence(request, company_id):
    profile, _ = api_client.get_company_full_profile(company_id)
    data, error = api_client.get_competitive_intelligence(company_id)

    return render(request, 'companies/competitive_intelligence.html', {
        'company': profile,
        'data': data,
        'error': error,
        'active_tab': 'competitive',
    })


def financials_funding(request, company_id):
    profile, _ = api_client.get_company_full_profile(company_id)
    data, error = api_client.get_financials_funding(company_id)

    return render(request, 'companies/financials_funding.html', {
        'company': profile,
        'data': data,
        'error': error,
        'active_tab': 'financials',
    })


def contact_information(request, company_id):
    profile, _ = api_client.get_company_full_profile(company_id)
    data, error = api_client.get_contact_information(company_id)

    return render(request, 'companies/contact_information.html', {
        'company': profile,
        'data': data,
        'error': error,
        'active_tab': 'contact',
    })


def digital_presence(request, company_id):
    profile, _ = api_client.get_company_full_profile(company_id)
    data, error = api_client.get_digital_presence_brand(company_id)

    return render(request, 'companies/digital_presence.html', {
        'company': profile,
        'data': data,
        'error': error,
        'active_tab': 'digital',
    })


def partnerships_ecosystem(request, company_id):
    profile, _ = api_client.get_company_full_profile(company_id)
    data, error = api_client.get_partnerships_ecosystem(company_id)

    return render(request, 'companies/partnerships_ecosystem.html', {
        'company': profile,
        'data': data,
        'error': error,
        'active_tab': 'partnerships',
    })


def indygx_assessment(request, company_id):
    profile, _ = api_client.get_company_full_profile(company_id)
    data, error = api_client.get_indygx_assessment(company_id)

    return render(request, 'companies/indygx_assessment.html', {
        'company': profile,
        'data': data,
        'error': error,
        'active_tab': 'assessment',
    })
