from django.urls import path
from . import views

urlpatterns = [
    path('guestDashboard/', views.guestDashboard, name='guestDashboard'),
]
