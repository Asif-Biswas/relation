from django.urls import path,include
from . import views
from django.contrib.auth import views as auth_views 

app_name = "main"

urlpatterns = [
    path("", views.home, name="home"),
    path("register/", views.register, name="register"),
    path("login/", auth_views.LoginView.as_view(template_name="main/login.html"), name="login"),
    path("logout/", auth_views.LogoutView.as_view(template_name="main/register.html"), name="logout"),
    
]