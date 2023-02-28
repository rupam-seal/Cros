from tkinter.tix import Select
from ..core.models import *

from django import forms
from django.forms import ModelForm, TextInput, Select

from django.contrib.auth.forms import UserCreationForm
from django .contrib.auth.models import User


class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
