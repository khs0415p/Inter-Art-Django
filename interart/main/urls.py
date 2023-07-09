from django.urls import path
from .views import login_views, post_views, board_views, comment_views

app_name = 'main'

urlpatterns = [
    path('', login_views.login, name='login'),
    path('join/', login_views.join, name='join'),
    path('logout/', login_views.logout, name='logout'),
    
    path('home/', board_views.home, name='home'),
    path('board/', board_views.board, name='board'),
    path('my_home/', board_views.my_home, name='my_home'),
    path('notice/<int:notice_id>', board_views.notice, name='notice'),
    
    path('write/', post_views.write, name='write'),
    path('detail/<int:post_id>/', post_views.detail, name='detail'),
    path('post/modify/<int:post_id>/', post_views.post_modify, name='post_modify'),
    path('post/delete/<int:post_id>/', post_views.post_delete, name='post_delete'),
    
    path('comment/modify/<int:comment_id>/', comment_views.comment_modify, name='comment_modify'),
    path('comment/delete/<int:comment_id>/', comment_views.comment_delete, name='comment_delete'),
    path('like/<int:post_id>/', comment_views.likes, name='likes'),
]
