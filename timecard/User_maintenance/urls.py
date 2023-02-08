from django.urls import path
from . import views


urlpatterns = [
    path("show_user/", views.ShowProjectList.as_view(), name="show_user_list"),
    path("add_new_user/", views.AddNewUser.as_view(), name="add_new_user"),
]
