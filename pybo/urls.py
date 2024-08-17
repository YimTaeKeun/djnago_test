from django.urls import path
from pybo import views

app_name = 'pybo'
urlpatterns = [
    path('', views.index, name='home'),
    path('writePost/', views.write_post, name='write_post'),
    path('postView/<int:question_id>/', views.view_post, name='view_post'),
]