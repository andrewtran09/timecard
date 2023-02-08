from django.urls import path
from . import views


urlpatterns = [
    path("show_equipment_list/", views.ShowList.as_view(), name="show_equipment_list"),
    path("add_new_equipment/", views.AddNew.as_view(), name="add_new_equipment"),
]