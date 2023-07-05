from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.core.paginator import Paginator
from .forms import JoinForm, LoginForm, PostForm, CommentForm
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.contrib import messages
from .models import Post, Comment


# Create your views here.

# Login page (Home)
def login(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        _next = request.POST['next']
        if form.is_valid():
            user = form._meta.model.objects.get(username=request.POST['username'])
            auth_login(request, user)
            # request.session['user'] = form._meta.model.objects.get(username=request.POST['username']).pk
            return redirect(_next)
        
    else:
        form = LoginForm()
        _next = request.GET.get('next', 'home/')
    return render(request, 'main/login.html', {'form': form , 'next': _next})


# Logout
def logout(request):
    auth_logout(request)
    return redirect("main:login")


# Join (Sign-up)
def join(request):
    if request.method == "POST":
        form = JoinForm(request.POST)
        if form.is_valid():
            form.save()
            
            return redirect('/')

    else:
        form = JoinForm()
    
    return render(request, 'main/join.html', {"form": form})


# Home
def home(request):
    # 기간 내 최다 좋아요 Top-10
    # 기간 내 등록된 글이 없다면? 이 아니라 기간, 좋아요 정렬 top-10으로 하면댐
    top_post = Post.objects.all().order_by('-created_at')[:12]
    top_post = sorted(top_post, key=lambda x:-x.like_user.count())
    
    return render(request, 'main/home.html', {"top_post": top_post})


# Board
def board(request):
    
    page = request.GET.get('page', '1')
    kw = request.GET.get('kw', '')
    post_list = Post.objects.all().order_by('-created_at')
    print('kw', kw, 'page',page)
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


# Write
def write(request):
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            post.save()
            
            return redirect('main:board')
    else:
        
        form = PostForm()
    return render(request, 'main/write.html', {"form": form})


# Detail
def detail(request, post_id):
    
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.user = request.user
            _post = get_object_or_404(Post, pk=post_id)
            comment.post = _post
            comment.save()
            # return
        
    _post = Post.objects.get(id = post_id)
    return render(request, 'main/detail.html', {'post': _post})


# Post Modify
@login_required(login_url='main:login')
def post_modify(request, post_id):
    _post = get_object_or_404(Post, pk=post_id)
    if request.user != _post.user:
        messages.error(request, "수정권한이 없습니다.")
        return redirect('main:detail', post_id=post_id)
    
    if request.method == "POST":
        form = PostForm(request.POST, instance=_post)
        if form.is_valid():
            _post.save()
            return redirect('main:detail', post_id=post_id)
        
    form = PostForm(instance=_post)
    return render(request, 'main/write.html', {"form": form})


# Post Delete
@login_required(login_url='main:login')
def post_delete(request, post_id):
    _post = get_object_or_404(Post, pk=post_id)
    if request.user != _post.user:
        messages.error(request, "삭제권한이 없습니다.")
        return redirect('main:detail', post_id=post_id)
    _post.delete()
    return redirect('main:my_home')

# Comment Modify
@login_required(login_url='main:login')
def comment_modify(request, comment_id):
    comment = get_object_or_404(Comment, pk=comment_id)
    
    if request.user != comment.user:
        messages.error("수정권한이 없습니다.")
        return redirect("main:detail", post_id=comment.post.id)
    
    if request.method == "POST":
        form = CommentForm(request.POST, instance=comment)
        if form.is_valid():
            comment = form.save()
            return redirect("main:detail", post_id=comment.post.id)
    form = CommentForm(instance=comment)
    return render(request, 'main/comment_modify.html', {"form": form})


# Comment Delete
@login_required(login_url='main:login')
def comment_delete(request, comment_id):
    comment = get_object_or_404(Comment, pk=comment_id)
    if request.user != comment.user:
        messages.error(request, "삭제권한이 없습니다.")
        return redirect('main:detail', post_id=comment.post.id)
    comment.delete()
    return redirect('main:detail', post_id=comment.post.id)

# Like
@login_required(login_url='main:login')
def likes(request, post_id):
    
    _post = get_object_or_404(Post, pk=post_id)
    if _post.like_user.filter(pk=request.user.pk).exists():
        _post.like_user.remove(request.user)
    else:
        _post.like_user.add(request.user)
    
    return redirect(f'/main/detail/{post_id}')

