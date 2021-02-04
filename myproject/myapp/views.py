from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth
from django.http import HttpResponseRedirect
from django.contrib import messages
from .forms import RegisterForm
from .models import Register

def add(request):
    return render(request, 'add.html', {"name": "Ankita"}) 

def result(request):
    if request.method=="POST":
        n1 = request.POST.get('n1')
        n2 = request.POST.get('n2')
        r = int(n1) + int(n2)
        return render(request, 'result.html', {"result": r}) 


def signup(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        password = request.POST['password']
        re_password = request.POST['re_password']
        if password == re_password:
            user = Register.objects.create_user(name=name, username=email, email=email, password=password)
            user.save()
            messages.success(request,'user created sucessfully')
            return redirect('login')
        else:
            form = RegisterForm()
            messages.error(request,'user not created')
            return render(request, 'signup.html')
    return render(request, 'signup.html')

def login(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST.get('password')
        #remember_me = request.POST.get('remember_me')
        user = auth.authenticate(username = email, password = password)

        if user is not None:
            auth.login(request, user)
            messages.success(request,"sucessfully login")
            return redirect('/')
        else:
            messages.error(request, 'Invalid Email or Password.')
            return redirect('login')

    else:
        return render(request, 'login.html')

def index(request):
    return render(request, 'index.html')

def logout(request):
    auth.logout(request)
    return render(request, 'index.html')