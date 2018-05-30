from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
    return HttpResponse("Hello World!")

def fapp(request):
    return HttpResponse("<h1>fapping</h1>")
