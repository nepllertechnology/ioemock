from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

def home(request):
    return render(request, 'firstapp/index.html')

def register(request):
    if request.method == 'POST':
        username = request.POST['fullname']  # We’ll treat 'fullname' as the username
        email = request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']

        if password == confirm_password:
            user = User.objects.create_user(username=username, email=email, password=password)
            user.save()
            return redirect('login')
        else:
            return render(request, 'firstapp/register.html', {'error': 'Passwords do not match!'})

    return render(request, 'firstapp/register.html')

def login_view(request):
    if request.method == 'POST':
        username = request.POST['fullname']  # Again, treat 'fullname' as the username
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('dashboard')
        else:
            return render(request, 'firstapp/login.html', {'error': 'Invalid username or password'})

    return render(request, 'firstapp/login.html')

@login_required(login_url='/login/')
def dashboard(request):
    return render(request, 'firstapp/dashboard.html')

def logout_view(request):
    logout(request)
    return redirect('home')
