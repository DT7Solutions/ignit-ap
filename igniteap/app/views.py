# from urllib import request
from datetime import datetime
from django.contrib import messages
from django.http import JsonResponse
from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import StudentIdeaform,EventTimer,Event,AgendaDay,EventTimer,Contact,Collaboration,Speakers
from django.contrib.auth import authenticate,login,logout

# Create your views here.


 

def Login(request):
    if request.method == 'POST':
        username = request.POST.get('u_name','')
        password= request.POST.get('ps_word','')
        user = authenticate(username=username,password=password)
        if user is not None and user.is_active:
            oUser = login(request, user)
            print(oUser)
            return JsonResponse({'success': True})

        return JsonResponse({'success': False, 'error': 'invalid user credentials'})
            
    return render(request ,'uifiles/login.html') 


def logout_view(request):
    logout(request)
    return redirect('/')


def Home(request):
    timercount = EventTimer.objects.first()
    x =  timercount
    print('message ok',timercount)
    events = Event.objects.filter(activeEvent="active").order_by("-ID", "activeEvent")[:3]
    return render(request ,'uifiles/index.html',{"EventTimer":timercount,"event":events}) 


def About(request):
    return render(request ,'uifiles/about.html') 

def speakers(request):
    speakers = Speakers.objects.all()  
    return render(request, 'uifiles/speakers.html', {'speakers': speakers})

def events(request):
    events = Event.objects.all().order_by("-ID")
    return render(request ,'uifiles/events.html',{"event":events}) 

def contact(request):
    if request.method == 'POST':
        firstname = request.POST.get('firstname','')
        lastname = request.POST.get('lastname','')
        email = request.POST.get('email','')
        phone = request.POST.get('phone','')
        message = request.POST.get('message','')

        oContact = Contact(Firstname=firstname, Lastname=lastname,Email=email,Phone=phone,Message=message)
        oContact.save()
        return JsonResponse({'success':True})
    return render(request ,'uifiles/contact.html') 



def Partners(request):
    if request.method == 'POST':
        firstname = request.POST.get('firstname',"")
        lastname = request.POST.get('lastname',"")
        email = request.POST.get('email',"")
        phone = request.POST.get('phone',"")
        brand_agency = request.POST.get('barand',"")
        industry = request.POST.get('industry',"")
        collaboration_Type = request.POST.get('Collaboration_Type',"")
        oApplication = Collaboration(FirstName=firstname,LastName=lastname,Email=email,Phone=phone,Brand_Agency=brand_agency ,Industry=industry,Collaboration_Type=collaboration_Type)
        oApplication.save()
        return JsonResponse({'success': True})
 
    return render(request ,'uifiles/collaborations.html') 


def userRegister(request):
    if request.method == "POST":
        firstname = request.POST.get('firstname','')
        lastname = request.POST.get('lastname', '')
        email = request.POST.get('email', '')
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        confirm_pass = request.POST.get('confirm_password', '')
        if password == confirm_pass:
            # oUser = User.objects.filter(username=user_name)
            oUser = User.objects.filter(username=username).first()
            if oUser is None:
                oRegister = User.objects.create_user(first_name=firstname,last_name=lastname,email=email,username=username,password=password)
                oRegister.save()
                return JsonResponse({'success': True})
            return JsonResponse({'success': False, 'error': 'User already exists'})
        return JsonResponse({'success': False, 'error': 'Passwords do not match'})

    return render(request ,'uifiles/user-registration.html') 


# @login_required
def studentIdea_form(request):
    student_submit = StudentIdeaform.objects.filter(user=request.user)
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

        oStudentform = StudentIdeaform(Firstname=firstname,Lastname=lastname,Address=address,Email=email,Phone=phone,College_Name=colleg_name,Branch_Name=branchname,Idea_Description=ideadescription,user=request.user,Upload_url=uploadurl,file=up_file)
        oStudentform.save()

        messages.success(request, 'Student details added successfully')
    
    return render(request ,'uifiles/student-idea-submission.html',{'student_submit':student_submit}) 



def Event_detail(request,slug):
    event_info= Event.objects.get(slug=slug)
    agenda_dates= AgendaDay.objects.filter(event=event_info)

    return render(request, 'uifiles/events-details.html',{"eventinfo":event_info,"agenda":agenda_dates})



