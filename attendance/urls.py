from django.urls import path
from . import views

urlpatterns = [
    path('', views.attendance_reports, name='attendance_reports'),
    path('checkin/', views.checkin, name='checkin'),
    path('checkout/<int:pk>/', views.checkout, name='checkout'),
]
