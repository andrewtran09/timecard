from django.urls import path
from . import views


urlpatterns = [
    path("show_project/", views.ShowProjectList.as_view(), name="show_project_list"),
    path("add_new_project/", views.AddNewProject.as_view(), name="add_new_project"),
]
