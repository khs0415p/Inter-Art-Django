from django.shortcuts import render
from django.core.paginator import Paginator
from django.db.models import Q
from ..models import Post



# Home
def home(request):
    
    top_post = Post.objects.all().order_by('-created_at')[:12]
    top_post = sorted(top_post, key=lambda x:-x.like_user.count())
    
    return render(request, 'main/home.html', {"top_post": top_post})


# Board
def board(request):
    
    page = request.GET.get('page', '1')
    kw = request.GET.get('kw', '')
    post_list = Post.objects.all().order_by('-created_at')
    if kw:
        post_list = post_list.filter(
            Q(title__icontains=kw) |
            Q(content__icontains=kw) |
            Q(user__username__icontains=kw) |
            Q(comment__user__username__icontains=kw) |
            Q(comment__comment__icontains=kw)
        ).distinct()
        
    paginator = Paginator(post_list, 10)
    page_obj = paginator.get_page(page)
    
    return render(request, 'main/board.html', {'post_list': page_obj, 'page':page, 'kw': kw})


# My Home
def my_home(request):
    
    post_list = Post.objects.filter(user_id=request.user.pk).order_by('-created_at')
    return render(request, 'main/my_home.html', context={"post_list": post_list})
