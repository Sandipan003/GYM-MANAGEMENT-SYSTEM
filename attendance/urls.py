from django.urls import path
from . import views

urlpatterns = [
    path('', views.attendance_reports, name='attendance_reports'),
    path('checkin/', views.checkin, name='checkin'),
    path('checkout/<int:pk>/', views.checkout, name='checkout'),
    path('edit/<int:pk>/', views.attendance_edit, name='attendance_edit'),
    path('delete/<int:pk>/', views.attendance_delete, name='attendance_delete'),
]
