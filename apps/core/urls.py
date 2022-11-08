from django.urls import path
from . import views

urlpatterns = [
    # -------- Admin -------- #
    path('', views.dashboard, name='dashboard'),
    path('orders/', views.orders, name='orders'),
    path('ordersPaid/', views.ordersPaid, name='ordersPaid'),
    path('ordersPending/', views.ordersPending, name='ordersPending'),
    path('category/', views.category, name='category'),
    path('items/<str:pk>', views.items, name='items'),
    path('customers/', views.customers, name='customers'),
    path('create/', views.create, name='create'),
    path('removeOrder/<str:pk>', views.removeOrder, name='removeOrder'),
    path('removeItem/<str:pk>', views.removeItem, name='removeItem'),
]
