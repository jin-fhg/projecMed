"""projectMed URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, re_path
from django.contrib.auth import views as authviews
from projectMain import views as mainView
from projectMain.forms import LoginForm

urlpatterns = [
    path('admin/', admin.site.urls),
    path('dashboard/', mainView.dashboard, name='dashboard'),
    path('newsfeed/', mainView.newsfeed, name='newsfeed'),
    path('appointments/', mainView.appointment, name='appointment'),
    path('patients/', mainView.patients, name='patients'),
    path('sign-in/', authviews.LoginView.as_view(template_name='projectMain/sign-in.html'), name = 'sign-in'),
    path('sign-up/', mainView.signup, name='sign-up'),
    path('reset-password/', authviews.PasswordResetView.as_view(template_name='projectMain/forgot-password.html'),
         name='forgotpw'),
    path('password-reset/done/',
         authviews.PasswordResetDoneView.as_view(template_name='projectMain/password_reset_done.html'),
         name='password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>/',
         authviews.PasswordResetConfirmView.as_view(template_name='projectMain/password_reset_confirm.html'),
         name='password_reset_confirm'),
    path('password-reset-complete/',
         authviews.PasswordResetCompleteView.as_view(template_name='projectMain/password_reset_complete.html'),
         name='password_reset_complete'),
    re_path(r'^activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',mainView.activate, name='activate')

]
