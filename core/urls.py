from django.urls import path
from .views import *


urlpatterns = [
    path('client/list', list_client, name='client-list'),
    path('client/detail/<int:pk>', detail_client, name='client-detail'),
    path('client/create', create_client, name='client-create'),
    path('client/delete/<int:pk>', delete_client, name='client-delete'),

    path('employee/list', list_employee, name='employee-list'),
    path('employee/detail/<int:pk>', detail_employee, name='employee-detail'),
    path('employee/create', create_employee, name='employee-create'),
]
