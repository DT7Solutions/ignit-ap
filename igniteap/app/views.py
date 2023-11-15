from urllib import request
from django.contrib import messages
from django.shortcuts import render,redirect
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from .models import StudentIdeaform

# Create your views here.

def Home(request):
    if request.method == 'POST':
        username = request.POST.get('username','')
        password = request.POST.get('password','')
        user = authenticate(username=username, password=password)

        if user is None:
            print("login successfully")
            return redirect("/")
        else:
            print("invalid user credentials")
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
            print("conform password does not match ")

    return render(request ,'uifiles/user-registration.html') 



def studentIdea_form(request):
    if request.method == 'POST':
        firstname = request.POST.get('firstname','')
        lastname = request.POST.get('lastname','')
        address = request.POST.get('address','')
        email = request.POST.get('email','')
        phone = request.POST.get('phone','')
        collegname = request.POST.get('collegname','')
        branchname = request.POST.get('branchname','')
        ideadescription = request.POST.get('ideadescription','')
        up_file = request.FILES['pdfdocument']
        uploadurl = request.POST.get('uploadurl','')

        oStudentform = StudentIdeaform(Firstname=firstname,Lastname=lastname,Address=address,Email=email,Phone=phone,College_Name=collegname,Branch_Name=branchname,Idea_Description=ideadescription,Upload_url=uploadurl,file=up_file)
        oStudentform.save()

        messages.success(request, 'Student details added successfully')
    
    return render(request ,'uifiles/student-idea-submission.html') 