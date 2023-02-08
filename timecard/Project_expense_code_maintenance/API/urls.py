from django.urls import path
from .views import *


urlpatterns = [
    path("expense_code_list/", expense_list, name="expense_code_list"),
    path("expense_code_list/<int:pk>", expense_list_detail, name="expense_code_list_detail"),
]