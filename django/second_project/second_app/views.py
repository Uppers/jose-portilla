from django.shortcuts import render
from django.http import HttpResponse
from second_app.models import User
from . import forms
# Create your views here.


def index(request):
    return HttpResponse("Homepage")

def second_app(request):
    title = {'page_title':'This is the Second App'}
    return render(request, "second_app/help_page.html", context= title)

def help(request):
    title = {'page_title': 'This is the Help Page'}
    return render(request, "second_app/help_page.html", context= title) 

def users(request):
    user_list = User.objects.order_by('first_name')
    users = {'user_table':user_list}
    return render(request, "second_app/index.html", context = users)

def user_data_input(request):
    form = forms.PersonalData()

    if request.method == "POST":
        form = forms.PersonalData(request.POST)

        if form.is_valid():
        # CAN DO THIS
            user =  User.objects.get_or_create(
                                                first_name=form.cleaned_data['first_name']  
                                                ,last_name=form.cleaned_data['last_name']
                                                ,email= form.cleaned_data['email']
                                            )[0]
            user.save()
            # THIS CLEARS THE FORM IF SUCCESSFUL
            form = forms.PersonalData()
        # OR THIS
        # form.save(commit=True)
        # return index(request)
        
    return render(request, "second_app/user_data_form.html", {'form':form})