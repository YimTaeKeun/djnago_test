from django.urls import path
from . import views

urlpatterns = [
    path('', views.getPeople, name='getPeople'),
    path('human/<int:id>/', views.getHuman, name='getHuman'),
]