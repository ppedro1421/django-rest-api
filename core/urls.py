from django.urls import path
from .views import *


urlpatterns = [
    # EMPLOYER
    path('employer/list', list_employer, name='employer-list'),
    path('employer/detail/<str:pk>', detail_employer, name='employer-detail'),
    path('employer/create', create_employer, name='employer-create'),
    path('employer/update/<str:pk>', update_employer, name='employer-update'),
    path('employer/delete/<str:pk>', delete_employer, name='employer-delete'),

    # ROLE
    path('role/list', list_role, name='role-list'),
    path('role/detail/<str:pk>', detail_role, name='role-detail'),
    path('role/create', create_role, name='role-create'),
    path('role/update/<str:pk>', update_role, name='role-update'),
    path('role/delete/<str:pk>', delete_role, name='role-delete'),

    # EMPLOYEE
    path('employee/list', list_employee, name='employee-list'),
    path('employee/detail/<str:pk>', detail_employee, name='employee-detail'),
    path('employee/create', create_employee, name='employee-create'),
    path('employee/update/<str:pk>', update_employee, name='employee-update'),
    path('employee/delete/<str:pk>', delete_employee, name='employee-delete'),
]
