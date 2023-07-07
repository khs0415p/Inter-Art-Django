from django.shortcuts import render, redirect
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from ..forms import JoinForm, LoginForm



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
        print(request.POST)
        form = JoinForm(request.POST)
        if form.is_valid():
            form.save()
            
            return redirect('/')

    else:
        form = JoinForm()
    
    return render(request, 'main/join.html', {"form": form})