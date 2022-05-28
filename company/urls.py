from django.urls import path
from company.views import CompanyListCreate, CompanyRetrieve

urlpatterns = [
    path('companies', CompanyListCreate.as_view(), name="companylistcrate"),
    path('companies/<str:name>', CompanyRetrieve.as_view(), name="companyretrieve")
]
