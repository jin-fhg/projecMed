from django.contrib.auth.views import logout_then_login
from django.shortcuts import render
# Create your views here.
from django.shortcuts import render, redirect
from .forms import userForm, profileForm, patientForm, clinicForm
from django.urls import reverse
from django.contrib.auth.decorators import login_required


#For Email Verification
from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes, force_text
from django.contrib.auth import login
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.template.loader import render_to_string
from .tokens import account_activation_token
from django.contrib.auth.models import User
from django.core.mail import EmailMessage
from django.http import HttpResponse, Http404

#Message Notification Alert
from django.contrib import messages

from django.http import JsonResponse
#Authenticatio response
from django.contrib.auth import authenticate, login
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import json

# Error Logger
import logging

#import from models
from .models import *

#Instantiate Error Logging
logger = logging.getLogger(__name__)

@login_required
def dashboard(request):
    if request.method == 'POST':
        form = profileForm(request.POST, instance=request.user.account)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    else:
        form = profileForm(instance=request.user.account)

    if request.method == 'POST' and not form.is_valid():
        cform = clinicForm(request.POST, instance=request.user.account)
        if cform.is_valid():
            cform.save()
            return redirect('dashboard')
    else:
        cform = clinicForm()
        instance = request.user.account
        showclinic = Clinic.objects.filter(account_id = instance)
        context = {'form': form,
                   'cform': cform,
                    'showclinic': showclinic
                   }
    return render(request, 'projectMain/dashboard.html', context)

@login_required
def appointment(request):
    return render(request, 'projectMain/appointment.html')

@login_required
def newsfeed(request):
    return render(request, 'projectMain/newsfeed.html')

@login_required
def patients(request):
    if request.method == 'POST':
        pform = patientForm(request.POST)
        if pform.is_valid():
            patient = pform.save(commit=False)
            patient.save()
            patient.doctor.add(request.user.account)
            return redirect('patient')
    else:
        pform = patientForm()

    return render(request, 'projectMain/patient.html', {'pform': pform})

@login_required
def profile(request):
    if request.method == 'POST':
        form = profileForm(request.POST, request.FILES, instance=request.user.account)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    else:
        form = profileForm(instance=request.user.account)

    return render(request, 'projectMain/profile.html', {'form': form})

@csrf_exempt
def signin(request):
    return render(request, 'projectMain/sign-in.html')


def signup(request):
    if request.method == 'POST':
        form = userForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_staff = False
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')

            user.save()
            user.accounttype.access = 1
            current_site = get_current_site(request)
            mail_subject = 'Activate your Account.'
            message = render_to_string('projectMain/acc_active_email.html', {
                'user': user,
                'domain': current_site.domain,
                'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                'token': account_activation_token.make_token(user),
            })
            to_email = form.cleaned_data.get('email')
            email = EmailMessage(mail_subject, message, to=[to_email])
            email.send()
            messages.success(request, f'Please confirm your registration by going to your email')
            return redirect('sign-in')
    else:
        form = userForm()
    return render(request, 'projectMain/sign-up.html', {'form': form})

def activate(request, uidb64, token):
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None
    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()
        login(request, user)
        return redirect('dashboard')
        #return HttpResponse('Thank you for your email confirmation. Now you can login your account.')
    else:
        return HttpResponse('Activation link is invalid!')

def forgotpw(request):

    return render(request, 'projectMain/forgot-password.html')

@login_required
def logout(request):
    return logout_then_login(request, reverse('sign-in'))

logger = logging.getLogger(__name__)

def auth(request):
    if request.method == 'POST':
        uname = request.headers.get('Username')
        pword = request.headers.get('Password')

        # logger.error(uname)
        # logger.error(pword)
        # logger.error(request.POST)
        # logger.error(request.headers)
        # logger.error(request.body)
        user = authenticate(username=uname, password=pword)
        if user is not None:
            if user.is_active:
                login(request, user)
                return HttpResponse(json.dumps({"message": "LOGIN_SUCCESS"}), content_type="application/json")
            else:
                return HttpResponse(json.dumps({"message": "inactive"}), content_type="application/json")
        else:
            return HttpResponse(json.dumps({"message": "invalid"}), content_type="application/json")
    return HttpResponse('')




def addPatient(request):

    return render(request,'projectMain/patient-profile.html')


def addClinic(request):
    if request.method == 'POST':
        cform = clinicForm(request.POST, instance=request.user.account)
        if cform.is_valid():
            logger.error(request.POST)
            logger.error(request.user.account)
            cform.save()
            logger.error(cform)
            return redirect('dashboard')
    else:
        cform = clinicForm()

    return render(request,'projectMain/addClinic.html', {'cform': cform})