from django.urls import path
from .views import *


urlpatterns = [
    path("equipment_code_list/", ecm_list, name="equipment_code_list"),
    path("equipment_code_list/<int:pk>", ecm_list_detail, name="equipment_code_list_detail"),
]
