from django.urls import path
from . import views

urlpatterns = [
    path('staffDashboard/', views.staffDashboard, name='staffDashboard'),
]
