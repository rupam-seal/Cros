from django.urls import path
from . import views

urlpatterns = [
    path('staffs/', views.staff, name='staffs'),
]
