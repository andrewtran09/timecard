from django.urls import path
from .views import json_labor_list, api_labor_detail, LaborList

urlpatterns = [
    path('json_all_labor/', json_labor_list, name='api_json_all_labors'),
    path('labors/vfs_detail/<int:pk>', api_labor_detail, name='labors_vfs_detail'),
    path('', LaborList.as_view(), name='labor_list'),
]