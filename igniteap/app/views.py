from urllib import request
from django.contrib import messages
from django.http import JsonResponse
from django.shortcuts import render,redirect
# from django.contrib.auth import authenticate, login,logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import StudentIdeaform,EventTimer
from datetime import datetime, timedelta
from .models import StudentIdeaform
from django.contrib import auth

# Create your views here.

def Home(request):
    timercount = EventTimer.objects.first()
    x =  timercount
    print('message ok',timercount)
    if request.method == 'POST':
        username = request.POST.get('username','')
        password = request.POST.get('password','')
        user = auth.authenticate(username=username, password=password)

        if user is None:
            print("login successfully")
            return redirect("/")
        else:
            print("invalid user credentials") 
       
    return render(request ,'uifiles/index.html',{"EventTimer":timercount}) 
    # if request.method == 'POST':
    #     user_name = request.POST.get('username','')
    #     user_password = request.POST.get('password','')
    #     oUser= User.objects.all()
    #     for oItem in oUser:
    #         if oItem.username==user_name and oItem.password==user_password:
    #             # user = login(request, user)
    #             print(oItem.username)
    #             return JsonResponse({'success': True})
    #     return JsonResponse({'success': False, 'error': 'invalid user credentials'})
            
    return render(request ,'uifiles/index.html') 

def Login(request):
    if request.method == 'POST':
        u_name = request.POST.get('u_name','')
        ps_word = request.POST.get('ps_word','')
        # aUser = User.objects.all()
        # oUser = auth.authenticate(request,username=u_name,password=ps_word)
        # if oUser is not None:
        #     oUser = auth.login(request, oUser)
        #     print(oUser)
        #     return JsonResponse({'success': True})
        
        oUser= User.objects.all()
        for oItem in oUser:
            if oItem.username==u_name and oItem.password==ps_word:
                # user = auth.login(request, user)
                # print(oItem.username)
                return JsonResponse({'success': True})
        return JsonResponse({'success': False, 'error': 'invalid user credentials'})
            
    return render(request ,'uifiles/login.html') 

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
                return JsonResponse({'success': True})
            else:
                return JsonResponse({'success': False, 'error': 'User already exists'})
        else:
            return JsonResponse({'success': False, 'error': 'Passwords do not match'})

    return render(request ,'uifiles/user-registration.html') 



def studentIdea_form(request):
    student_submit = StudentIdeaform.objects.all()
    if request.method == 'POST':
        firstname = request.POST.get('firstname','')
        lastname = request.POST.get('lastname','')
        address = request.POST.get('address','')
        email = request.POST.get('email','')
        phone = request.POST.get('phone','')
        colleg_name = request.POST.get('collagename','')
        branchname = request.POST.get('branchname','')
        ideadescription = request.POST.get('ideadescription','')
        up_file = request.FILES['pdfdocument']
        uploadurl = request.POST.get('uploadurl','')

        oStudentform = StudentIdeaform(Firstname=firstname,Lastname=lastname,Address=address,Email=email,Phone=phone,College_Name=colleg_name,Branch_Name=branchname,Idea_Description=ideadescription,Upload_url=uploadurl,file=up_file)
        oStudentform.save()

        messages.success(request, 'Student details added successfully')
    
    return render(request ,'uifiles/student-idea-submission.html') 

# views.py




# def countdown_view(request):
#     countdown = Countdown.objects.first()
#     if countdown:
#         target_datetime = datetime.combine(countdown.target_date, datetime.min.time())
       
        
#         current_datetime = datetime.now()
#         remaining_time = target_datetime - current_datetime
#         remaining_days = remaining_time.days
#         remaining_hours, remainder = divmod(remaining_time.seconds, 3600)
#         remaining_minutes, remaining_seconds = divmod(remainder, 60)
#     else:
#         remaining_days = remaining_hours = remaining_minutes = remaining_seconds = None
#     print("Remaining Days:", remaining_days)
#     print("Remaining Hours:", remaining_hours)
#     print("Remaining Minutes:", remaining_minutes)
#     print("Remaining Seconds:", remaining_seconds)

#     return render(request, 'uifiles/index.html', {
#         'remaining_days': remaining_days,
#         'remaining_hours': remaining_hours,
#         'remaining_minutes': remaining_minutes,
#         'remaining_seconds': remaining_seconds,
#     })
#         return JsonResponse({'success': True})
       
#     return render(request ,'uifiles/student-idea-submission.html',{'student_submit':student_submit}) 
