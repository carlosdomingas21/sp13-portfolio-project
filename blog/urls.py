from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    path('',views.home, name='blog-name'),
    path('<int:blog_id>/', views.detail, name='detail'),
]