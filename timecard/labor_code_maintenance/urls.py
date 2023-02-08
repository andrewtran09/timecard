from django.urls import path
from . import views


urlpatterns = [
    path("show_lc_list/", views.ShowList.as_view(), name="show_lc_list"),
    path("add_new_lc/", views.AddNew.as_view(), name="add_new_lc"),
]
