from django.urls import path
from .import views

urlpatterns = [
    path('order/',views.order, name='order'),
    path('order_view/', views.order_view, name='order_view'), 
    path('order/<str:food_name>/', views.order_now, name='order_now'),
    path('submit_order/', views.order_submit, name='order_submit'),
    path('burgar/<str:burgar_name>/', views.burgar, name='burgar'),
    path('pizza/<str:pizza_name>/', views.pizza, name='pizza'),
    path('pasta/<str:pasta_name>/', views.pasta, name='pasta'),
    path('fries/<str:fries_name>/', views.fries, name='fries'),
    path('samosa/<str:samosa_name>/', views.samosa,name='samosa'),
    path('content/', views.content, name='content'),
    path('chicken/<str:food_item>/', views.chicken_view, name='chicken'),

     
]