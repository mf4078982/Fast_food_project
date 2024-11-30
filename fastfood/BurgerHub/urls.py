from django.urls import path
from . import views

urlpatterns = [
    path('menu/', views.menu_list, name='menu_list'),
    path('menu/add/', views.add_item, name='add_item'),
    path('menu/edit/<int:pk>/', views.edit_item, name='edit_item'),
    path('menu/delete/<int:pk>/', views.delete_item, name='delete_item'),
]
