from django.contrib import admin
from .models import Companies


class CompaniesAdmin(admin.ModelAdmin):
    list_display=['company_id','company_name','company_domain','year_founded','industry','size_range','locality','country','linked_in_url','current_employee_est','total_employee_est']


admin.site.register(Companies,CompaniesAdmin)

