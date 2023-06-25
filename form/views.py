from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate,login
from django.contrib.auth.decorators import login_required

# Create your views here.
def registration(request):
    if request.method=='POST':
        username=request.POST.get('name')
        email=request.POST.get('email')
        password=request.POST.get('pass')
        if User.objects.filter(username__iexact=username).exists():
            messages.info(request,"Username already used")
        else:
            data=User.objects.create_user(username,email,password)
            data.save()
            messages.info(request,"You are Registered")
            return redirect('signin')
    return render(request,'registration.html')
    

def signin(request):
    if request.method=='POST':
        username=request.POST.get('name')
        password=request.POST.get('pass')
        data=authenticate(request,username=username,password=password)
        if data is not None:
            login(request,data)
            messages.info(request,"You have signin")
            return redirect('homepage')
        else:
            messages.info(request,"You are typing Email or password wrong ")
    return render(request,'signin.html')

@login_required(login_url='signin')
def homepage(request):
    return render(request,'Homepage.html')