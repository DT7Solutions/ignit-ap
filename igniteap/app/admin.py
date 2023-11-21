from django.utils.html import format_html
from django.contrib import admin
from .models import StudentIdeaform,EventTimer,Event,AgendaDay,Panelist,Contact,Collaboration



# Register your models here.


class AdminStudentForm(admin.ModelAdmin):
    list_display = ('Firstname','Lastname','Address','Email','Phone','College_Name','Branch_Name','Idea_Description','Upload_url_link','file','Approved','Date')
    def Upload_url_link(self, obj):
        return format_html('<a href="{}" target="_blank">{}</a>', obj.Upload_url, obj.Upload_url)

    Upload_url_link.short_description = 'Upload_url'
    Upload_url_link.allow_tags = True

class AdminEvent(admin.ModelAdmin):
     list_display = ('title','description','date','location','image')

class AdminAgendaDay(admin.ModelAdmin):
     list_display = ('event','date','date')

class AdminPanelist(admin.ModelAdmin):
     list_display = ('agenda_day','name','designation','companeyName','image')    

class AdminCountdown(admin.ModelAdmin):
    list_display = ('EventName','target_datetime')

class AdminContact(admin.ModelAdmin):
    list_display= ('Firstname','Lastname','Email','Phone','Message')

class AdminCollaborationForm(admin.ModelAdmin):
    list_display=('FirstName','LastName','Email' ,'Phone','Brand_Agency','Industry','Collaboration_Type')
    list_filter= ['Date']


admin.site.register(StudentIdeaform,AdminStudentForm)
admin.site.register(EventTimer,AdminCountdown)
admin.site.register(Event,AdminEvent)
admin.site.register(AgendaDay,AdminAgendaDay)
admin.site.register(Panelist,AdminPanelist)
admin.site.register(Contact,AdminContact)
admin.site.register(Collaboration,AdminCollaborationForm)




