
from django.urls import path,include
from .views import *

app_name='web'

urlpatterns = [
    path('',home,name='home'),
    path('about/',about,name='about'),
    path('branch/',branch,name='branch'),
    path('contact/',contact,name='contact'),
    path('doctor/',doctor,name='doctor')
]
