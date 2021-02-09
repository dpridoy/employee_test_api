from django.contrib import admin
from .models import Company, Department, Employee

# Register your models here.


class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('empCode', 'name', 'phone', 'status', 'department', 'company', 'address')
    search_fields = ('empCode', 'name', 'status')


admin.site.register(Company)
admin.site.register(Department)
admin.site.register(Employee, EmployeeAdmin)
