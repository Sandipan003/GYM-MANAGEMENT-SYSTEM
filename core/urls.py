from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('staff/', views.dashboard, name='staff'),
    path('login-success/', views.login_success, name='login_success'),
]
