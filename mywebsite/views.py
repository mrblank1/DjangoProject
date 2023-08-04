from django.shortcuts import render
from django.http import HttpResponse
def http_test(request):
    return HttpResponse("<h1>hello</h1>")
def home(request):
    return render(request,'website/index.html')
def contact(request):
    return render(request,'website/contact.html')
def about(request):
    return render(request,'website/about.html')
def elements(request):
    return render(request,'website/elements.html')
# Create your views here.
