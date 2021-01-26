from django.shortcuts import redirect
from django.urls import path
from django.contrib.auth import views as auth_views
from .forms import UserLoginForm
from . import views

app_name = 'accounts'

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(template_name="registration/login.html", 
                        authentication_form=UserLoginForm, redirect_authenticated_user=True), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('register/', views.RegistrationView.as_view(), name='register'),
    path('profile/', views.ProfileView.as_view(), name='profile')

]