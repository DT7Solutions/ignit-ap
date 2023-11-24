from django.urls import path
from .views import Home,About,contact,userRegister,studentIdea_form,Login,logout_view,Event_detail,Speakers,Partners,events

urlpatterns = [
    path('', Home, name="Home"),
    path('about/', About, name="About"),
    path('speakers/', Speakers, name="speakers"),
    path('partners/', Partners, name="partners"),
    path('contact/', contact, name="contact"),
    path('login/', Login, name="login"),
    path('register/', userRegister, name="register"),
    path('studentideaform/', studentIdea_form, name='ideaform'),
    path('logout/', logout_view, name='logout'),
    path('events/',events,name="events"),
    path('event-details/<str:slug>/', Event_detail, name='event-details'),

]
