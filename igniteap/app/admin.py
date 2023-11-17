from django.utils.html import format_html
from django.contrib import admin
from .models import StudentIdeaform,EventTimer



# Register your models here.


class AdminStudentForm(admin.ModelAdmin):
    list_display = ('Firstname','Lastname','Address','Email','Phone','College_Name','Branch_Name','Idea_Description','Upload_url_link','file','Approved','Date')
    def Upload_url_link(self, obj):
        return format_html('<a href="{}" target="_blank">{}</a>', obj.Upload_url, obj.Upload_url)

    Upload_url_link.short_description = 'Upload_url'
    Upload_url_link.allow_tags = True

class AdminCountdown(admin.ModelAdmin):
    list_display = ('EventName','target_datetime')

admin.site.register(StudentIdeaform,AdminStudentForm)
admin.site.register(EventTimer,AdminCountdown)




# class AdminRegistration(admin.ModelAdmin):
#     list_display = ('Firstname','Lastname','Email','Username','Password','Confirm_pass')

# admin.site.register(Registration, AdminRegistration)