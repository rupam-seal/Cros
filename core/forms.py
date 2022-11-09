from tkinter.tix import Select
from .models import *

from django import forms
from django.forms import ModelForm, TextInput, Select

from django.contrib.auth.forms import UserCreationForm
from django .contrib.auth.models import User

class OrderForm(ModelForm):
    class Meta:
        model = Order
        fields = '__all__'

        widgets = {
            'customer': Select(attrs={
                'class': "form__select-inp",
            }),
            'item': Select(attrs={
                'class': "form__select-inp",
            }),
            'price': TextInput(attrs={
                'class': "form__inp",
            }),
            'quantity': TextInput(attrs={
                'class': "form__inp",
            }),
            'status': Select(attrs={
                'class': "form__select-inp",
            }),

        }

class ItemForm(ModelForm):
    # USERS = ()
    # u = User.objects.all()
    # for user in u:
    #     if user.groups.all()[0].name == 'customer':
    #         USERS += (user.username, user.username)
    #         print('======', USERS)

    # user = forms.ChoiceField(choices=USERS)
    class Meta:
        model = Item
        fields = '__all__'

        widgets = {
            'name': TextInput(attrs={
                'class': "form__inp",
            }),
            'price': TextInput(attrs={
                'class': "form__inp",
            }),
            'quantity': TextInput(attrs={
                'class': "form__inp",
            }),
            'category': Select(attrs={
                'class': "form__select-inp",
            }),
            'tag': Select(attrs={
                'class': "form__select-inp",
            }),

        }

class CategoryForm(ModelForm):
    class Meta:
        model = Category
        fields = '__all__'
        widgets = {
            'name': TextInput(attrs={
                'class': "form__inp",
            }),
            'quantity': TextInput(attrs={
                'class': "form__inp",
            }),
            'status': Select(attrs={
                'class': "form__select-inp",
            }),
        }

class TagForm(ModelForm):
    class Meta:
        model = Tag
        fields = '__all__'
        widgets = {
            'name': TextInput(attrs={
                'class': "form__inp",
            }),
        }

class CreateUserForm(UserCreationForm):
    class Meta :
        model = User
        fields = ['username', 'email', 'password1', 'password2']