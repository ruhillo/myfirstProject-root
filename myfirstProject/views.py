from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    return render(request,'home.html',{"word":"hello"})

def about(request):
    return HttpResponse('<h1>About page</h1>')