from django.contrib import admin
from .models import *


class ClientAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'cnpj', 'created_at']

class ClientEmployeeAdmin(admin.ModelAdmin):
    list_display = ['id', 'employer', 'first_name', 'last_name', 'cpf', 'created_at']

admin.site.register(Client, ClientAdmin)
admin.site.register(ClientEmployee, ClientEmployeeAdmin)
