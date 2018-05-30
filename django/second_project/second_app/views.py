from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def index(request):
    return HttpResponse("Homepage")

def second_app(request):
    title = {'page_title':'This is the Second App'}
    return render(request, "second_app/help_page.html", context= title)

def help(request):
    title = {'page_title': 'This is the Help Page'}
    return render(request, "second_app/help_page.html", context= title) 
