from django.contrib import admin
from .models import StudentIdeaform

# Register your models here.


class AdminStudentForm(admin.ModelAdmin):
    list_display = ('Firstname','Lastname','Address','Email','Phone','College_Name','Branch_Name','Idea_Description','Upload_url','file','Approved','Date')



admin.site.register(StudentIdeaform,AdminStudentForm)




# class AdminRegistration(admin.ModelAdmin):
#     list_display = ('Firstname','Lastname','Email','Username','Password','Confirm_pass')

# admin.site.register(Registration, AdminRegistration)