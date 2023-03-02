from ..core.models import *

from django.forms import ModelForm, TextInput, Select, PasswordInput

from django.contrib.auth.forms import UserCreationForm
from django .contrib.auth.models import User


class CustomerForm(ModelForm):
    class Meta:
        model = Customer
        fields = ['name', 'email', 'phone', 'gender']
        widgets = {
            'name': TextInput(attrs={
                'class': "form__inp",
            }),
            'email': TextInput(attrs={
                'class': "form__inp",
            }),
            'phone': TextInput(attrs={
                'class': "form__inp",
            }),
            'gender': Select(attrs={
                'class': "form__select-inp",
            }),
        }


class StaffForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        widgets = {
            'username': TextInput(attrs={
                'class': "form__inp",
            }),
            'email': TextInput(attrs={
                'class': "form__inp",
            }),
            'password1': PasswordInput(attrs={
                'class': "form__inp",
            }),
            'password2': PasswordInput(attrs={
                'class': "form__inp",
            }),
        }
