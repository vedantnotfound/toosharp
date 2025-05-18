from django.contrib import admin
from .models import Employee, EmployeePosition

class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'email', 'department', 'position', 'mobile_number')
    search_fields = ('first_name', 'last_name', 'email')
    list_filter = ('department', 'position', 'gender')

admin.site.register(Employee, EmployeeAdmin)

admin.site.register(EmployeePosition)