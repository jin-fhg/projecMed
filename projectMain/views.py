from django.shortcuts import render
# Create your views here.
from django.shortcuts import render



def dashboard(request):
    return render(request, 'projectMain/dashboard.html')

def appointment(request):
    return render(request, 'projectMain/appointment.html')


def newsfeed(request):
    return render(request, 'projectMain/newsfeed.html')

def patients(request):
    return render(request, 'projectMain/patient.html')

def signin(request):
    return  render(request, 'projectMain/sign-in.html')

def signup(request):
    return render(request, 'projectMain/sign-up.html')


def forgotpw(request):
    return render(request, 'projectMain/forgot-password.html')