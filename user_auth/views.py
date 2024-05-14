from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login as auth_login, logout as auth_logout
from .forms import UserRegisterForm

def register(request):
    if request.method == "POST":
        register_form = UserRegisterForm(request.POST)
        if register_form.is_valid():
            register_form.save()
            return redirect('dashboard')
    else:
        register_form = UserRegisterForm()

    context = {
        'register_form': register_form
        }
    return render(request, 'user_auth/register.html', context)

def login(request):
    if request.method == "POST":
        login_form = AuthenticationForm(request, request.POST)
        if login_form.is_valid():
            user = login_form.get_user()
            auth_login(request, user)
            return redirect('dashboard')
    else:
        login_form = AuthenticationForm()

    context = {
        'login_form': login_form
        }
    return render(request, 'user_auth/login.html', context)

def logout(request):
    auth_logout(request)
    return render(request, 'user_auth/logout.html')
