from django.urls import path
from . import views


urlpatterns = [
    path("show_sc_list/", views.ShowList.as_view(), name="show_sc_list"),
    path("add_new_sc/", views.AddNew.as_view(), name="add_new_sc"),
]
