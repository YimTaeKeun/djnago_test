from django.urls import path
from blog import views

app_name = 'blog'

urlpatterns = [
    path('', views.index, name='blog_home'),
    path('postview/<int:post_id>/', views.view_post, name='view_post'),
    path('create_post/', views.create_post, name='create_post'),
    path('submit_comment/<int:post_id>/', views.submit_comment, name='submit_comment'),
]