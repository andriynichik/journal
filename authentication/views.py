# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.forms.utils import ErrorList
from django.http import HttpResponse
from .forms import LoginForm, SignUpForm
from .models import User
from django.contrib.auth.decorators import login_required
from django.contrib import messages


def login_view(request):
    form = LoginForm(request.POST or None)

    msg = None

    if request.method == "POST":

        if form.is_valid():
            email = form.cleaned_data.get("email")
            password = form.cleaned_data.get("password")
            check = User.objects.filter(email=email).first()
            if  check:
                user = authenticate(username=check.username, password=password)
            else:
                user = None
            if user is not None:
                login(request, user)
                return redirect("/")
            else:    
                msg = 'Не вірно вказані дані авторизації'
        else:
            msg = 'Помилка валідації'

    return render(request, "accounts/login.html", {"form": form, "msg" : msg})

def register_user(request):

    msg     = None
    success = False

    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            email = form.cleaned_data.get("email")
            raw_password = form.cleaned_data.get("password1")
            user = authenticate(email=email, password=raw_password)

            msg    = 'User created - please <a href="/login">login</a>.'
            success = True
            
            #return redirect("/login/")

        else:
            msg = 'Form is not valid'    
    else:
        form = SignUpForm()

    return render(request, "accounts/register.html", {"form": form, "msg" : msg, "success" : success })
@login_required
def UsersList(request):
    transactions = User.objects.all()
    data = {'transactions': transactions}
    return render(request, 'app/useus/users_list.html',context=data)


@login_required
def UserCreate(request):
    data = {}
    form = SignUpForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            messages.success(request, 'Користувача створено')
            return redirect('/users/list')
    data['form'] = form
    return render(request, 'app/useus/user_create.html', data)