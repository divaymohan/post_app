from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    full_name = forms.CharField(max_length=100)

    class Meta:
        model = User
        fields = ['username', 'full_name', 'email',  'password1', 'password2']
