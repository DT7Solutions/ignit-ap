from django.contrib import admin
from .models import Registration
# Register your models here.
class AdminRegistration(admin.ModelAdmin):
    list_display = ('Firstname','Lastname','Email','Username','Password','Confirm_pass')

admin.site.register(Registration, AdminRegistration)