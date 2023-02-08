from django.urls import path
from django.contrib.auth import views as auth_views
from . import views


urlpatterns = [
    path('login/', auth_views.LoginView.as_view(template_name='useradmin/login.html'), name='useradmin_login'),
    path('logout/', auth_views.LogoutView.as_view(), name='useradmin_logout'),

]
