from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm

class RegisterationForm(UserCreationForm):
    email = forms.EmailField(label='email',widget=forms.EmailInput(attrs={'placeholder':'Email'}))
    username = forms.CharField(label='username',widget=forms.TextInput(attrs={'placeholder':'username'}))
    password1 = forms.CharField(label='password',widget=forms.PasswordInput(attrs={'placeholder':'password'}))
    password2 = forms.CharField(label='confirm password',widget=forms.PasswordInput(attrs={'placeholder':'confirm password'}))
    class Meta:
        model = User
        fields = ['username','email','password1','password2']



class CustomAuthForm(AuthenticationForm):
    username = forms.CharField(label='username',widget=forms.TextInput(attrs={'placeholder':'username'}))
    password = forms.CharField(label='password',widget=forms.PasswordInput(attrs={'placeholder':'password'}))
