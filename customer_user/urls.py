from django.urls import path
from . import views

urlpatterns = [
        # ---------- Customer ----------- #
    path('customerDashboard/', views.customerDashboard, name='customerDashboard'),
    path('customerOrders/', views.customerOrders, name='customerOrders'),
    path('customerOrdersPaid/', views.customerOrdersPaid, name='customerOrdersPaid'),
    path('customerOrdersPending/', views.customerOrdersPending, name='customerOrdersPending'),
]