from . views import *
from django.urls import path

urlpatterns=[

    path('user_maintenance/userrole/<int:pk>',userrole,name='user_role'),
    path('user_maintenance/role_view', RoleList.as_view(), name='role_list'),
    path('user_maintenance/usermain/<int:pk>', usermain, name='user_maintenance'),
    path('user_maintenance/maint_view',MaintList.as_view(),name='maint_list'),


]