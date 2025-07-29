from django.urls import path
from . import views

urlpatterns = [
    path('protected_view/', views.protected_view, name='protected_view'),
    path('', views.index, name='index'),
]