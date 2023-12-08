from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from . models import Place,Team

# Create your views here.
def demo(request):
    obj=Place.objects.all()
    obj1 = Team.objects.all()
    return render(request,"index.html",{'result':obj,'result1':obj1})

def register(request):
    if request.method=='POST':
        username = request.POST['username']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        password = request.POST['password']
        cpassword = request.POST['confirmpassword']
        if password==cpassword:
            if User.objects.filter(username=username).exists():
                 messages.info(request,'username is already taken.')
                 return redirect('register')
            elif User.objects.filter(email=email).exists():
                 messages.info(request,'email is already taken.')
                 return redirect('register')
            else:
                 user=User.objects.create_user(username=username,first_name=first_name,last_name=last_name,password=password,email=email)
                 user.save();
                 return redirect("login")
                 print("user created")
        else:
            messages.info(request,"password not matched")
            return redirect('register')
        return redirect('/')
    return render(request,"register.html")
def login(request):
    if request.method == 'POST':
        username=request.POST['username']
        password=request.POST['password']
        user=auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('/')
        else:
            messages.info(request,"invalid login credentials")
            return redirect("login")

    return render(request,"login.html")
def logout(request):
    auth.logout(request)
    return redirect('/')
def about(request):
    return render(request,"about.html")
