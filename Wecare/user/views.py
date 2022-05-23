from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def home(re):
    return render(re,'user/mainpage.html')

def special(re):
    return render(re,'user/specialization.html')

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