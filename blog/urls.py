from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    path('detail/<int:pk>/', views.new_detail, name='new_detail'),
    path('new/', views.new_blog, name='new_blog')
]