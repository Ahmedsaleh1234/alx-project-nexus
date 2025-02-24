from django.shortcuts import render, redirect
from django.contrib.auth.models import User
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
            return redirect('home')

    return render(req, 'login.html')