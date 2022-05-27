from django.shortcuts import render,redirect
from django.http import HttpResponse
#from .models import UserRegister
#from .forms import Formreg
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect


# Create your views here.
def index(request):
    return render(request,'home.html') 
def home(request):
    return render(request,'home.html')
def register(request): 
   return render(request, 'register.html')
       
def signup(request):
    if request.method == 'POST':
        username=request.POST['username']
        email=request.POST['email']
        password=request.POST['psw']
        user=User.objects.create_user(username=username,password=password,email=email)
        user.save()
    return redirect("/signinpage/")
def loginpage(request):
    return render(request,'signin.html')
def signin(request):
    if request.method=='POST':
        username=request.POST['name']
        password=request.POST['password']
        user= authenticate(request, password=password, username=username)
        if user is not None:
            login(request,user)
            return redirect("/")
        else:
            return redirect("/signinpage/")

def logout_user(request):
    logout(request)
    return redirect("/signinpage/")
def potter(request):
    return render(request,"pottery.html")

