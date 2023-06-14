from django.shortcuts import render
# Create your views here.
from django.shortcuts import render
# Create your views here.
from django.contrib.auth.models import User, auth
from django.shortcuts import render, redirect, HttpResponse
from django.contrib import messages
from django.contrib.auth import login,logout

def index(request):
    return render(request,"index.html")
def register1(request):
    if request.method == 'POST':
        user_name = request.POST['Username']
        pass1 = request.POST['password1']
        pass2 = request.POST['password2']
        if pass1==pass2:
            if User.objects.filter(username=user_name).exists():
                messages.info(request,"Username taken")
            else:
                user = User.objects.create_user(user_name, pass1, pass2)
                user.save()
                return redirect('login')
        else:
            messages.info(request,"Passwords are not matching")
            return redirect('register1')
    return render(request, "register1.html")

def login(request):
    if request.method == 'POST':
        user_name1 = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(request,username=user_name1,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('loggedin')
        else:
            messages.info(request,"Invalid credentials")
            return redirect('login')
    return render(request,"login.html")
def loggedin(request):

    return render(request,"loggedin.html")
def regform(request):
    if request.method == 'POST':
         f_name = request.POST['firstname']
         l_name = request.POST['lastname']
         age = request.POST['age']
         male = request.POST['male']
         female =request.POST['female']
         others= request.POST['other']
         country_code = request.POST['country code']
         phone = request.POST['phone']
         address = request.POST['address']
         email = request.POST['email']
         user= User.objects.create_user(f_name,l_name,age,male,female,others,country_code,phone,address,email)
         user.save()
         return render(request,"confirm.html")
    return render(request,"regform.html")

def logout(request):
    if request.method == 'POST':
        auth.logout(request)
        return redirect('/')
def confirm(request):
    return render(request,"confirm.html")