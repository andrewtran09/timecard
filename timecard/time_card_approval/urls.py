from django.urls import path
from . import views


urlpatterns = [
    path("show_time_cards_list/", views.ShowList.as_view(), name="show_time_cards_list"),
    path("add_new_time_card/", views.AddNew.as_view(), name="add_new_time_card"),
]
