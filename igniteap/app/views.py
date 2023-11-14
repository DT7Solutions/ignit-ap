from urllib import request
from django.contrib import messages
from django.shortcuts import render
from django.contrib.auth.models import User

# Create your views here.

def Home(request):
    return render(request ,'uifiles/index.html') 

def About(request):
    return render(request ,'uifiles/about.html') 

def contact(request):
    return render(request ,'uifiles/contact.html') 

def userRegister(request):
    if request.method == "POST":
        firstname = request.POST.get('firstname','')
        lastname = request.POST.get('lastname', '')
        email = request.POST.get('email', '')
        user_name = request.POST.get('username', '')
        password = request.POST.get('password', '')
        confirm_pass = request.POST.get('confirm_password', '')
        if password == confirm_pass:
            # oUser = User.objects.filter(username=user_name)
            oUser = User.objects.filter(username=user_name).first()
            if oUser is None:
                oRegister = User(first_name=firstname,last_name=lastname,email=email,username=user_name,password=password)
                oRegister.save()
            else:
                # messages.success(request, "user is allreddy exited ")
                print("user is allreddy exited")
        else:
            # messages.success(request, "conform password doe's not match !")
            print("conform password doe's not match ")

    return render(request ,'uifiles/user-registration.html') 