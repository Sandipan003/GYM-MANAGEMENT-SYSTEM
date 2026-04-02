from django.urls import path
from . import views

urlpatterns = [
    path('', views.member_list, name='member_list'),
    path('add/', views.member_add, name='member_add'),
    path('<int:pk>/', views.member_detail, name='member_detail'),
    path('<int:pk>/edit/', views.member_edit, name='member_edit'),
    path('<int:pk>/delete/', views.member_delete, name='member_delete'),
    path('dashboard/', views.member_dashboard, name='member_dashboard'),
    path('performance/', views.member_attendance_history, name='member_attendance'),
    path('membership/', views.member_plans, name='member_plans'),
    path('membership/pay/<int:plan_id>/', views.process_plan_payment, name='process_plan_payment'),
    path('attendance/toggle/', views.toggle_attendance, name='toggle_attendance'),
    path('signup/', views.signup, name='signup'),
]
