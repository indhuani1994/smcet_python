from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def mysite(request):
    return HttpResponse("<h1>Welcome to Student</h1>")
def home(request):
    return render(request,"home.html")
def about(request):
    return render(request,"about.html")
def contact(request):
    return render(request,"contact.html")
def gallery(request):
    return render(request,"gallery.html")
def register(request):
    return render(request,"register.html")