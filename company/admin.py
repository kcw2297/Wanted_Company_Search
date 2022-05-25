from django.contrib import admin
from company.models import CompanyInfo, Tag, Company


admin.site.register(CompanyInfo)
admin.site.register(Tag)
admin.site.register(Company)
