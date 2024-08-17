from django.urls import path
from . import views

app_name = 'APINetwork'

urlpatterns = [
    path('', views.host, name='index'),
]