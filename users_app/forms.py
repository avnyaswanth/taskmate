from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User

class CustomRegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)
    # first_name = forms.CharField(max_length=100)
    # last_name = forms.CharField(max_length=100)
    class Meta:
        model = User
        fields = ['username','email','password1','password2']