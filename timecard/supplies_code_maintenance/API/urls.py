from django.urls import path
from .views import *


urlpatterns = [
    path("supplies_code_list/", sc_list, name="supplies_code_list"),
    path("supplies_code_list/<int:pk>", sc_list_detail, name="supplies_code_list_detail"),
]
