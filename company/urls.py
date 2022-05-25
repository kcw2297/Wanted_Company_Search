from django.urls import path
from company.views import CompanyAuto

urlpatterns = [
    path('companies', CompanyAuto.as_view(), name="company_auto"),
    # path('companies/<str:name>'),
    # path('search', search.as_view())
]