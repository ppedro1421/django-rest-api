from django.contrib import admin
from .models import *


class EmployerAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'created_at']


class EmployeeAdmin(admin.ModelAdmin):
    list_display = ['id', 'employer', 'first_name', 'last_name', 'role', 'created_at']


class RoleAdmin(admin.ModelAdmin):
    list_display = ['id', 'employer', 'description']


admin.site.register(Employer, EmployerAdmin)
admin.site.register(Employee, EmployeeAdmin)
admin.site.register(Role, RoleAdmin)
