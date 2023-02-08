from django.urls import path
from . import views


urlpatterns = [
    path("show_project_expense_list/", views.ShowList.as_view(), name="show_project_expense_list"),
    path("add_new_project_expense/", views.AddNew.as_view(), name="add_new_project_expense"),
]