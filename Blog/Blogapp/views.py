from django.shortcuts import render

from django.contrib.auth import logout

# Create your views here.


def base(request):
    return render(request, 'base.html')


def home(request):
    return render(request, 'home.html')

def add_blog(request):
    return render(request, 'add_blog.html')
    

def login_view(request):
    return render(request, 'login.html')

def logout_view(request):
    logout(request)
    return redirect('/')


def register_view(request):
    return render(request, 'register.html')
