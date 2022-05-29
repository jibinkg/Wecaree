from django.shortcuts import render
from django.http import HttpResponse
from .models import bookingform
# Create your views here.
def home(re):
    try:
        s=bookingform.objects.all()
        # print(s)
    except:
        print('hai')
    return render(re,'user/mainpage.html', {'data':s})

def sundepart(re):
    x=re.POST.get('name')
    print(x,'xxxxxxxxxxx')
    return render(re,'user/sunrisedepartments.html')

def doctor(re):
    return render(re,'user/doctorslist.html')

def booking(re):
    return render(re,'user/bookingform.html')

def reciept(re):
    return render(re,'user/reciept.html')

def login(re):
    return render(re,'user/registration/signin.html')

def signup(re):
    return render(re,'user/registration/signup.html')

def amaladepart(re):
    return render(re,'user/amaladepartments.html')

def elitedepart(re):
    return render(re,'user/elitedepartments.html')

def jubiliedepart(re):
    return render(re,'user/jubiliedepartments.html')

def westfortdepart(re):
    return render(re,'user/westfortdepartments.html')