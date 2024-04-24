from django.urls import path
from .views import *


urlpatterns = [
    # EMPLOYER
    path('employer/list', list_employer, name='employer-list'),
    path('employer/detail/<int:pk>', detail_employer, name='employer-detail'),
    path('employer/create', create_employer, name='employer-create'),
    path('employer/update/<int:pk>', update_employer, name='employer-update'),
    path('employer/delete/<int:pk>', delete_employer, name='employer-delete'),

    # ROLE
    path('role/list', list_role, name='role-list'),
    path('role/detail/<int:pk>', detail_role, name='role-detail'),
    path('role/create', create_role, name='role-create'),
    path('role/update/<int:pk>', update_role, name='role-update'),
    path('role/delete/<int:pk>', delete_role, name='role-delete'),

    # EMPLOYEE
    path('employee/list', list_employee, name='employee-list'),
    path('employee/detail/<int:pk>', detail_employee, name='employee-detail'),
    path('employee/create', create_employee, name='employee-create'),
    path('employee/update/<int:pk>', update_employee, name='employee-update'),
    path('employee/delete/<int:pk>', delete_employee, name='employee-delete'),
]
