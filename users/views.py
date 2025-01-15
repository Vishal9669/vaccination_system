from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib import messages
from .models import User
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
import time

def signup(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        password = request.POST.get('password')

        if User.objects.filter(username=username).exists():
            messages.error(request, 'Username already exists. Please choose another.')
        elif User.objects.filter(email=email).exists():
            messages.error(request, 'Email already exists. Please use another.')
        elif User.objects.filter(phone=phone).exists():
            messages.error(request, 'Phone number already exists. Please use another.')
        else:
            user = User.objects.create_user(username=username, email=email, phone=phone, password=password)
            user.save()
            messages.success(request, 'Account created successfully! Redirecting to login page...')
            return render(
                request, 
                'signup.html', 
                {'redirect': True, 'url': 'signin', 'delay': 5}  # Add redirect logic in the frontend
            )
    return render(request, 'signup.html')

def signin(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            messages.success(request, f'Welcome back, {user.username}!')
            return redirect('welcome')  # Redirect to the welcome page
        else:
            messages.error(request, 'Invalid username or password.')
    return render(request, 'signin.html')

@login_required
def welcome(request):
    return render(request, 'welcome.html', {'username': request.user.username})

def logout_view(request):
    logout(request)
    return redirect('signin')