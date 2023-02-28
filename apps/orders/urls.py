from django.urls import path
from . import views

urlpatterns = [
    path('orders/', views.orders, name='orders'),
    path('ordersPaid/', views.ordersPaid, name='ordersPaid'),
    path('ordersPending/', views.ordersPending, name='ordersPending'),
    path('removeOrder/<str:pk>', views.removeOrder, name='removeOrder'),
]
