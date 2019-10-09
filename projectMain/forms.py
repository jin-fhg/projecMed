from django.contrib.auth.models import User
from django import forms
from .models import Account

#login form template
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm

class userForm(UserCreationForm):
    #username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'name': 'namesurname',  'placeholder': 'Name Surname', 'type': 'text'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control', 'name': 'email',  'placeholder': 'Email Address', 'type': 'email'}))
    #password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'name': 'password',  'placeholder': 'Password', 'type': 'password', 'minlength': '6'}))
    #password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'name': 'confirm',  'placeholder': 'Confirm Password', 'type': 'password', 'minlength': '6'}))

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

    def __init__(self, *args, **kwargs):
        super(userForm, self).__init__(*args, **kwargs)

        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['username'].widget.attrs['placeholder'] = 'Name Surname'
        self.fields['password1'].widget.attrs['class'] = 'form-control'
        self.fields['password1'].widget.attrs['placeholder'] = 'Password'
        self.fields['password1'].widget.attrs['minlength'] = '6'
        self.fields['password2'].widget.attrs['class'] = 'form-control'
        self.fields['password2'].widget.attrs['placeholder'] = 'Confirm Password'
        self.fields['password2'].widget.attrs['minlength'] = '6'


class LoginForm(forms.ModelForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'name': 'username',  'placeholder': 'Usernametest', 'type': 'text'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'name': 'password', 'placeholder': 'Passwordtest', 'type': 'password'}))

    class Meta:
        model = User
        fields = ['username', 'password']
