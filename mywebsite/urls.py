
from django.urls import path
from mywebsite.views import  *
app_name='website'
urlpatterns = [
    path('http-test' , http_test),
    path('' , home,name='index'),
    path('contact' , contact,name='contact'),
    path('about', about, name ='about'),
    path('elements' , elements, name ='elements')
]
