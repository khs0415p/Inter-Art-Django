from django.shortcuts import render, redirect
from django.urls import reverse
from .forms import MemberForm, LoginForm

# Create your views here.

# Login page (Home)
def login(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            return redirect('main:board')
        
        
    else:
        form = LoginForm()
    return render(request, 'main/login.html', {'form': form})

# Join (Sign-up)
def join(request):
    if request.method == "POST":
        form = MemberForm(request.POST)
        
        if form.is_valid():
            form.save()
            return redirect('main:login')
    else:
        form = MemberForm()
    return render(request, 'main/join.html', {'form': form})

# Board (게시판)
def board(request):
    return render(request, 'main/board.html')
    