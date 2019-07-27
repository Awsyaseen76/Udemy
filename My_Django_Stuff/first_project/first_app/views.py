from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    return HttpResponse('Hello world....')

def index2(request):
    return HttpResponse("<h1 style='background-color:red'>Test</h1>")