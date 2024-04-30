from django import forms
from django.forms import ModelForm
from .models import User


class UserForm(forms.ModelForm):

    class Meta:
        model= User
        fields = ['usuario', 'email', 'clave', 'edad', 'pais']



class LoginForm(forms.Form):
    email = forms.EmailField(label='email')
    clave = forms.CharField(label='clave', widget=forms.PasswordInput)


