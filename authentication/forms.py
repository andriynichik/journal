# -*- encoding: utf-8 -*-


from django import forms
from .models import  User
from .models import USER_TYPE_CHOICES
from django.contrib.auth.forms import PasswordChangeForm

class LoginForm(forms.Form):
    email = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder" : "email",
                "class": "form-control"
            }
        ))
    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "placeholder" : "Пароль",
                "class": "form-control"
            }
        ))

class SignUpForm(forms.ModelForm):

    last_name = forms.CharField(
        label="ПІБ",
        widget=forms.TextInput(
            attrs={
                "placeholder" : "ПІБ",
                "class": "form-control"
            }
        ))
    username = forms.CharField(
        label="Логін",
        widget=forms.TextInput(
            attrs={
                "placeholder" : "Логін",
                "class": "form-control"
            }
        ))
    email = forms.EmailField(
        widget=forms.EmailInput(
            attrs={
                "placeholder" : "Email",                
                "class": "form-control"
            }
        ))
    password1 = forms.CharField(
        label="Пароль",
        widget=forms.PasswordInput(
            attrs={
                "placeholder" : "Пароль",
                "class": "form-control"
            }
        ))
    password2 = forms.CharField(
        label="Повторіть пароль",
        widget=forms.PasswordInput(

            attrs={
                "placeholder" : "Повторіть пароль",
                "class": "form-control"
            }
        ))

    role = forms.CharField(
        label="Роль користувача",
        widget=forms.Select( attrs={

                "class": "form-control"
            }, choices=USER_TYPE_CHOICES),
    )


    class Meta:
        model = User
        fields = ('last_name','username',  'password1', 'password2','email', 'role')



class MyPasswordChangeForm(forms.Form):

        old_password = forms.CharField(
            label="Старий пароль",
            widget=forms.PasswordInput(
                attrs={
                    "placeholder": "Старий пароль",
                    "class": "form-control"
                }
            ))
        password1 = forms.CharField(
            label="Новий пароль",
            widget=forms.PasswordInput(
                attrs={
                    "placeholder": "Новий пароль",
                    "class": "form-control"
                }
            ))
        password2 = forms.CharField(
            label="Повторіть пароль",
            widget=forms.PasswordInput(

                attrs={
                    "placeholder": "Повторіть пароль",
                    "class": "form-control"
                }
            ))

        class Meta:
            model = User
            fields = ('old_password', 'new_password1', 'new_password2')