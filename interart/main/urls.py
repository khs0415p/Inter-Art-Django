from django.urls import path
from . import views

app_name = 'main'

urlpatterns = [
    path('', views.login, name='login'),
    path('join/', views.join, name='join'),
    path('home/', views.home, name='home'),
    path('board/', views.board, name='board'),
    path('write/', views.write, name='write'),
    path('logout/', views.logout, name='logout'),
    path('my_home/', views.my_home, name='my_home'),
    path('detail/<int:post_id>/', views.detail, name='detail'),
]
