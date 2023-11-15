from django.urls import path
from .views import Home,About,contact,userRegister,studentIdea_form

urlpatterns = [
    path('', Home, name="Home"),
    path('about/', About, name="About"),
    path('contact/', contact, name="contact"),
    path('register/', userRegister, name="register"),
    path('ideaform/', studentIdea_form, name='ideaform'),

]
