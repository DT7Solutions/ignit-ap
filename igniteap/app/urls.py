from django.urls import path
from .views import Home,About,contact,userRegister,studentIdea_form,Login

urlpatterns = [
    path('', Home, name="Home"),
    path('about/', About, name="About"),
    path('contact/', contact, name="contact"),
    path('login/', Login, name="login"),
    path('register/', userRegister, name="register"),
    path('studentideaform/', studentIdea_form, name='ideaform'),

]
