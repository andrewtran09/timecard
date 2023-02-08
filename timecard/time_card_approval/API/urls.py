from django.urls import path
from .views import *

urlpatterns = [
    path('json_all_tcs/', json_TimeCardSub_list, name='api_json_all_projects'),
    path('tcs/vfs_detail/<int:pk>', api_time_card_detail, name='projects_vfs_detail'),
    path('tcs/', Time_Card_List.as_view(), name='project_list'),
    path('tcd/vfs_detail/<int:pk>', api_time_card_details_detail, name='projects_vfs_detail'),
    path('tcd/', Time_Card_Detail_List.as_view(), name='project_list'),
    path('tcstatus/vfs_detail/<int:pk>', api_time_card_status_detail, name='projects_vfs_detail'),
    path('tcstatus/', Time_Card_Status_List.as_view(), name='project_list'),
]