from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
    my_dict = {"insert_me": "<em>Hello I am from views.py!</em>"}
    return render(request, 'first_app/index.html', context=my_dict)

def fapp(request):
    return HttpResponse("<h1>fapping</h1>")
