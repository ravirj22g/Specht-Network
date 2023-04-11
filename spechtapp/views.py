from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout

# Create your views here.


def index(request):
    return render(request, 'home.html')
    # return HttpResponse("home page")


def profile(request):
    return render(request, 'profile.html')


def login_user(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password) 
        if user is not None:
            login(request, user)
            messages.info(request, f'{username}, You are logged in. ')
            return redirect("/")
        else:
            messages.info(request, 'Invalid username or password')

            return redirect('login')    
    return render(request, 'login.html')


def logout_user(request):
    return render(request, 'logout.html')


def signup_user(request):
    return render(request, 'signup.html')
