from django.http import HttpResponse
from django.shortcuts import render

def reverse(request):
    userText=str(request.GET['userText'])
    reversedUserText=userText[::-1]
    return render(request,'reverse.html',{"reversedUserText":reversedUserText,'userText':userText})

def home(request):
    return render(request,'home.html',{"word":"hello"})

def about(request):
    return HttpResponse('<h1>About page</h1>')