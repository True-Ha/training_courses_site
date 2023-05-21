from django import forms
from django.forms import TextInput, PasswordInput, Form, CharField

from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from .models import MyUser


# class MyUserCreationForm(UserCreationForm):
#     class Meta(UserCreationForm):
#         model = MyUser
#         fields = '__all__'
#
#
# class MyUserChangeForm(UserChangeForm):
#     class Meta(UserChangeForm):
#         model = MyUser
#         fields = ['tele_name', 'tele_username', 'email']
#


class LoginForm(Form):
    username = CharField(widget=TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Логин',
        'required': True
    }
    ))
    password = CharField(widget=PasswordInput(attrs={
        'class': 'form-control mt-2',
        'placeholder': 'Пароль',
        'required': True
    }
    ))


class UserUpdateForm(forms.ModelForm):
    username = forms.CharField(max_length=100,
                               required=True,
                               widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(required=True,
                             widget=forms.TextInput(attrs={'class': 'form-control'}))

    class Meta:
        model = MyUser
        fields = ['username', 'tele_username', 'email']


