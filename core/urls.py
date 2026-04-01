from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('facility/', views.facility_view, name='facility'),
    path('metrics/', views.metrics_view, name='metrics'),
    path('membership/', views.membership_view, name='membership'),
    path('staff/', views.dashboard, name='staff'),
    path('login-success/', views.login_success, name='login_success'),
]
