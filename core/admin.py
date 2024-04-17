from django.contrib import admin
from .models import *


class ClientAdmin(admin.ModelAdmin):
    list_display = ['name', 'cnpj']

admin.site.register(Client, ClientAdmin)
