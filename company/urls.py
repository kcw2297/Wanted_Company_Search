from django.urls import path
from company.views import CompanyListCreate

urlpatterns = [
    path('companies', CompanyListCreate.as_view(), name="company_auto"),
    # path('companies/<str:name>')
]
