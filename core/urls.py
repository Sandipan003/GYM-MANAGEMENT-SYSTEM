from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('facility/', views.facility_view, name='facility'),
    path('metrics/', views.metrics_view, name='metrics'),
    path('membership/', views.membership_view, name='membership'),
    path('staff/', views.dashboard, name='staff'),
    path('login-success/', views.login_success, name='login_success'),
    
    # Facility Management (Staff Only)
    path('facility/manage/', views.facility_manage, name='facility_manage'),
    path('facility/add/', views.facility_add, name='facility_add'),
    path('facility/<int:pk>/edit/', views.facility_edit, name='facility_edit'),
    path('facility/<int:pk>/delete/', views.facility_delete, name='facility_delete'),

    # Equipment Management (Staff Only)
    path('equipment/add/', views.equipment_add, name='equipment_add'),
    path('equipment/<int:pk>/edit/', views.equipment_edit, name='equipment_edit'),
    path('equipment/<int:pk>/delete/', views.equipment_delete, name='equipment_delete'),

    # Profile Management (Staff Only)
    path('profile/', views.profile_settings, name='profile_settings'),
]
