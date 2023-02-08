from django.urls import path
from . import views


urlpatterns = [
    #path("show_project_expense_list/", views.ShowList.as_view(), name="show_project_expense_list"),
    path("add_new_contract_rates/", views.AddNewForm, name="add_new_contract_rates"),
    path("add_new_contract_rates_page/", views.Add_New_Contract_Rate_Page, name='add_new_contract_rates_page')
]