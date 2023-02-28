from django.urls import path
from . import views

urlpatterns = [
    # -------- Admin -------- #
    path('category/', views.category, name='category'),
    path('items/<str:pk>', views.items, name='items'),
    path('removeItem/<str:pk>', views.removeItem, name='removeItem'),
]
