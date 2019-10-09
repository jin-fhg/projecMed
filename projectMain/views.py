from django.shortcuts import render
# Create your views here.
from django.shortcuts import render, redirect
from .forms import userForm, LoginForm

#For Email Verification
from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes, force_text
from django.contrib.auth import login, authenticate
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.template.loader import render_to_string
from .tokens import account_activation_token
from django.contrib.auth.models import User
from django.core.mail import EmailMessage
from django.http import HttpResponse, Http404

#Message Notification Alert
from django.contrib import messages

def dashboard(request):
    return render(request, 'projectMain/dashboard.html')

def appointment(request):
    return render(request, 'projectMain/appointment.html')


def newsfeed(request):
    return render(request, 'projectMain/newsfeed.html')

def patients(request):
    return render(request, 'projectMain/patient.html')

def signin(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)

    else:
        form = userForm()

    return  render(request, 'projectMain/sign-in.html')

def signup(request):
    if request.method == 'POST':
        form = userForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_staff = False
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')

            user.save()

            current_site = get_current_site(request)
            mail_subject = 'Activate your Farm Account.'
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