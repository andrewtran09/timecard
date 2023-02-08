from django.urls import path
from .views import json_project_list, api_project_detail, ProjectList

urlpatterns = [
    path('json_all_projects/', json_project_list, name='api_json_all_projects'),
    path('projects/vfs_detail/<int:pk>', api_project_detail, name='projects_vfs_detail'),
    path('', ProjectList.as_view(), name='project_list'),
]