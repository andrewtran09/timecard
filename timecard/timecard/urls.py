"""timecard URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from . import views


urlpatterns = [
    path("labor_code_maintenance/", include("labor_code_maintenance.urls")),
    path("supplies_code_maintenance/", include("supplies_code_maintenance.urls")),
    path("equipment_code_maintenance/", include("Equipment_code_maintenance.urls")),
    path("project_expense_code_maintenance/", include("Project_expense_code_maintenance.urls")),
    path("project_maintenance/", include("Project_Maintenance.urls")),
    path("user_maintenance/", include("User_maintenance.urls")),
    path("contract_rates/", include("Contract_Rates.urls")),
    path("user_admin/", include("useradmin.urls")),
    path("time_card_approval/", include("time_card_approval.urls")),
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('api/labors/', include('labor_code_maintenance.API.urls')),
    path('api/projects/', include('Project_Maintenance.API.urls')),
    path("api/equipment/", include("Equipment_code_maintenance.API.urls")),
    path("api/expense/", include("Project_expense_code_maintenance.API.urls")),
    path("api/supplies/", include("supplies_code_maintenance.API.urls")),
    path('api/contract_rates/', include('Contract_Rates.API.urls')),
    path('api/user_maintenance/', include('User_maintenance.API.urls')),
    path('api/timecard/', include('time_card_approval.API.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
