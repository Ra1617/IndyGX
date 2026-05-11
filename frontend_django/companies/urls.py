from django.urls import path
from . import views

app_name = 'companies'

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('companies/', views.company_list, name='company_list'),
    path('companies/<int:company_id>/', views.company_detail, name='company_detail'),
    path('companies/<int:company_id>/competitive-intelligence/', views.competitive_intelligence, name='competitive_intelligence'),
    path('companies/<int:company_id>/financials/', views.financials_funding, name='financials_funding'),
    path('companies/<int:company_id>/contact/', views.contact_information, name='contact_information'),
    path('companies/<int:company_id>/digital-presence/', views.digital_presence, name='digital_presence'),
    path('companies/<int:company_id>/partnerships/', views.partnerships_ecosystem, name='partnerships_ecosystem'),
    path('companies/<int:company_id>/assessment/', views.indygx_assessment, name='indygx_assessment'),
]
