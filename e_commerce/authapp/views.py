from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth
from django.contrib import messages
# Create your views here.
def signup(req):
    if req.method == 'POST':
        name = req.POST['name']
        password = req.POST['password']
        email = req.POST['email']
        if User.objects.filter(email=email).exists():
            messages.info(req, 'user already exist')
        else:
            User.objects.create_user(username=name, password=password, email=email)
            return redirect('login')

    return render(req, 'signup.html')
def login(req):
    if req.method == 'POST':
        email = req.POST['email']
        pas = req.POST['password']
        user = User.objects.get(email=email)
        user = auth.authenticate(username = user.username, password = pas)
        if user is not None:
            auth.login(req, user)
            return redirect('home')
        else:
            messages.info(req, 'username or password is not correct')
    return render(req, 'login.html')
def logout(req):
    auth.logout(req)
    
    return redirect('home')