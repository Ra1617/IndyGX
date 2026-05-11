from django.urls import path, include

urlpatterns = [
    path('', include('companies.urls')),
]
