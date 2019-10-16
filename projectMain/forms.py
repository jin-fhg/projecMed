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


class LoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super(LoginForm, self).__init__(*args, **kwargs)

    #username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'name': 'username',  'placeholder': 'Username', 'type': 'text', 'id': 'username'}))
    #password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'name': 'password', 'placeholder': 'Password', 'type': 'password',  'id': 'password'}))
        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['username'].widget.attrs['placeholder'] = 'UserName'
        self.fields['password'].widget.attrs['class'] = 'form-control'
        self.fields['password'].widget.attrs['placeholder'] = 'Password'


sex = [
    ('Male', 'Male'), ('Female', 'Female')

]

class profileForm(forms.ModelForm):
    firstname = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form-control', 'name': 'firstname', 'placeholder': 'First Name', 'type': 'text',
               'id': 'firstname'}))
    lastname = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control',
                                                             'name': 'lastname',  'placeholder': 'Last Name', 'type': 'text', 'id': 'lastname'}))
    middlename = forms.CharField(required=False,widget=forms.TextInput(attrs={'class': 'form-control', 'name': 'middlename',  'placeholder': 'Middle Name', 'type': 'text', 'id': 'middlename'}))
    suffix = forms.CharField(required=False, widget=forms.TextInput(attrs={'class': 'form-control', 'name': 'suffix',  'placeholder': 'Suffix', 'type': 'text', 'id': 'suffix'}))
    prefix = forms.CharField(required=False, widget=forms.TextInput(attrs={'class': 'form-control', 'name': 'prefix',  'placeholder': 'Prefix', 'type': 'text', 'id': 'prefix'}))
    sex = forms.CharField(widget=forms.Select(choices=sex, attrs={'class': 'regDropDown', 'name': 'sex',  'placeholder': 'Sex', 'type': 'select', 'id': 'sex'}))
    birthdate = forms.DateField(required=False, widget=forms.DateInput(attrs={'class': 'form-control', 'name': 'birthdate',  'placeholder': 'Birth Date', 'type': 'date', 'id': 'birthdate'}))
    birthplace = forms.CharField(required= False, max_length=100,
                                 widget=forms.TextInput(
                                     attrs={'class': 'form-control', 'name': 'birthplace', 'placeholder': 'Birth Place',
                                            'type': 'text', 'id': 'birthplace'})
                                 )



    class Meta:
        model = Account
        fields = ['image', 'firstname','lastname','middlename','suffix','prefix','sex','birthdate','birthplace']

