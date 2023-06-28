from django.urls import path
from . import views

app_name = 'main'

urlpatterns = [
    path('', views.login, name='login'),
    path('join/', views.join, name='join'),
    path('board/', views.board, name='board'),
]
