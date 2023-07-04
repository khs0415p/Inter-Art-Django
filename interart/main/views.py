from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from .forms import JoinForm, LoginForm, PostForm, CommentForm
from .models import User, Post
import json

# Create your views here.

# Login page (Home)
def login(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            user = form._meta.model.objects.get(username=request.POST['username'])
            auth_login(request, user)
            # request.session['user'] = form._meta.model.objects.get(username=request.POST['username']).pk
            return redirect('main:home')
        
    else:
        form = LoginForm()
    return render(request, 'main/login.html', {'form': form})

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
    # db에서 top10그림 뽑아서 앞으로 보내주기
    return render(request, 'main/home.html')

# Board
def board(request):
    post_list = Post.objects.all().order_by('-created_at')
    return render(request, 'main/board.html', {'post_list': post_list})


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
            comment.post = Post.objects.get(id=post_id)
            comment.save()
            # return
        
    _post = Post.objects.get(id = post_id)
    return render(request, 'main/detail.html', {'post': _post})