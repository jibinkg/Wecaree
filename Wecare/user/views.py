from django.shortcuts import render
from django.http import HttpResponse
from .models import bookingform
from .models import hospitalreg
from .models import doctorreg
from .models import login
# Create your views here.
def home(re):
    try:
        s=hospitalreg.objects.all()
        # print(s)
    except:
        print('hai')
    return render(re,'user/mainpage.html', {'data':s})

def sundepart(re):
    x=re.POST.get('name')
    print(x,'xxxxxxxxxxx')
    return render(re,'user/departments.html')

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


def new(re):
    return render(re,'user/home.html')