from django.shortcuts import render, redirect
from user.forms import RegisterForm
from user.forms import LoginForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.models import User
# Create your views here.

def register_view(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = RegisterForm()
        context = {
            'form': form
        }
        return render(request, "user/register.html",context)
    
def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get("password")
            user = authenticate(request, username=username,password=password)
            if user is not None:
                login(request, user)
                return redirect("home")
            else:
                messages.error(request, "Username or password is incorrect")
    form = LoginForm()
    context = {

        "form":form,
    }
    return render(request,"user/login.html", context)

def logout_views(request):
    logout(request)
    return redirect("home")