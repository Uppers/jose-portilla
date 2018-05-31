from django.shortcuts import render
from django.http import HttpResponse
from first_app.models import Topic, Webpage, AccessRecord
# Create your views here.

# def index(request):
#     my_dict = {"insert_me": "<em>Hello I am from views.py!</em>"}
#     return render(request, 'first_app/original_index.html', context=my_dict)

def index(request):
    webpages_list = AccessRecord.objects.order_by('date')
    date_dict = {'access_records':webpages_list}
    return render(request, 'first_app/index.html', context = date_dict)



def fapp(request):
    return HttpResponse("<h1>fapping</h1>")
