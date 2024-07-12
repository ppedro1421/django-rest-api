from django.urls import path
from .views import *


urlpatterns = [
    # EMPLOYER
    path('employer/list', list_employer, name='employer-list'),
    path('employer/get/<str:pk>', get_employer, name='employer-get'),
    path('employer/create', create_employer, name='employer-create'),
    path('employer/update/<str:pk>', update_employer, name='employer-update'),
    path('employer/delete/<str:pk>', delete_employer, name='employer-delete'),

    # EMPLOYEE
    path('employee/list', list_employee, name='employee-list'),
    path('employee/get/<str:pk>', get_employee, name='employee-get'),
    path('employee/create', create_employee, name='employee-create'),
    path('employee/update/<str:pk>', update_employee, name='employee-update'),
    path('employee/delete/<str:pk>', delete_employee, name='employee-delete'),
]
