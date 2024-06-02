from django.shortcuts import render, redirect
from user.forms import RegisterForm
from user.forms import LoginForm
from user.forms import ProfileForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

def register_view(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            password = form.cleaned_data.get('password')
            user.set_password(password)
            user.save()
            return redirect('home')
    else:
        form = RegisterForm()
    context = {
        'form': form
    }
    return render(request, "user/register.html", context)

    
def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        print(form)
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

@login_required(login_url="login_view")
def profile_view(request):
    if request.method == 'POST':
        form = ProfileForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('profile_view')
    form = ProfileForm(instance=request.user)
    return render(request, "user/profile.html",{'form':form})