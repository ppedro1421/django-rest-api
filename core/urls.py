from django.urls import path
from .views import *


urlpatterns = [
    path('client-list', list_client),
    path('client-detail/<int:id>', detail_client),
    path('client-create', create_client),
    path('client-delete/<int:id>', delete_client),

    path('employe-list', list_employe),
    path('employe-detail/<int:id>', detail_employe),
    path('employe-create', create_employe),
]
