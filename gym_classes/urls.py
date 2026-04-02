from django.urls import path
from . import views

urlpatterns = [
    # Member URLs
    path('', views.class_list, name='class_list'),
    path('book/<int:class_id>/', views.book_class, name='book_class'),
    path('unbook/<int:class_id>/', views.unbook_class, name='unbook_class'),
    
    # Staff URLs
    path('staff/', views.staff_class_list, name='staff_class_list'),
    path('staff/add/', views.staff_class_add, name='staff_class_add'),
    path('staff/<int:pk>/edit/', views.staff_class_edit, name='staff_class_edit'),
    path('staff/<int:pk>/delete/', views.staff_class_delete, name='staff_class_delete'),
]
