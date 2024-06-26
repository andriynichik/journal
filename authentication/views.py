# -*- encoding: utf-8 -*-


from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import PasswordChangeForm

from django.forms.utils import ErrorList
from django.http import HttpResponse
from .forms import LoginForm, SignUpForm, MyPasswordChangeForm
from .models import User
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from app.models import UserAgreement
from django.contrib.auth.hashers import check_password, make_password
from app.decorators import requires_role


def login_view(request):
    form = LoginForm(request.POST or None)
    agreement_text = UserAgreement.objects.filter().first()
    if  agreement_text is not None:
        text = agreement_text.text
    else:
        text = ''

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
                return redirect("/home")
            else:    
                msg = 'Не вірно вказані дані авторизації'
        else:
            msg = 'Помилка валідації'

    return render(request, "accounts/login.html", {"form": form, "agreement_text":text , "msg" : msg})

@login_required
def register_user(request):

    msg     = None
    success = False

    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():

            login = form.cleaned_data.get("login")
            email = form.cleaned_data.get("email")
            password = form.cleaned_data.get("password1")
            confirm_password = form.cleaned_data.get("password2")
            last_name = form.cleaned_data.get("last_name")
            role = form.cleaned_data.get("role")

            if password != confirm_password:
                messages.warning(request, 'Паролі не співпадають')
                return render(request, 'accounts/register.html', {'form': form})

            user = User.objects.create_user(login, email, password)
            user.role = role
            user.save()
            # form.save()
            # email = form.cleaned_data.get("email")
            # raw_password = form.cleaned_data.get("password1")
            # user = authenticate(email=email, password=raw_password)

            msg    = 'User created - please <a href="/login">login</a>.'
            success = True
            
            #return redirect("/login/")

        else:
            msg = 'Form is not valid'    
    else:
        form = SignUpForm()

    return render(request, "accounts/register.html", {"form": form, "msg" : msg, "success" : success })


@login_required
@requires_role(roles = ['security_admin', 'audit_admin'])
def UsersList(request):
    transactions = User.objects.all()
    data = {'transactions': transactions}
    return render(request, 'app/useus/users_list.html',context=data)


@login_required
@requires_role(roles = ['security_admin', 'audit_admin'])
def UserCreate(request):
    data = {}
    form = SignUpForm(request.POST or None)
    if request.method == 'POST':


        if form.is_valid():
            # login = form.cleaned_data.get("login")
            # email = form.cleaned_data.get("email")
            # password = form.cleaned_data.get("password1")
            # confirm_password = form.cleaned_data.get("password2")
            # last_name = form.cleaned_data.get("last_name")
            # role = form.cleaned_data.get("role")
            # if password != confirm_password:
            #     messages.warning(request, 'Паролі не відповідні')
            #     return render(request, 'accounts/register.html', {'form': form})
            #
            # user = User.objects.create_user(username=login, email=email,password=password)
            # user.role = role
            # user.last_name = last_name
            # user.save()
            user =  form.save(commit=False)
            user.is_active = True
            user.set_password(form.cleaned_data.get("password1"))
            user.last_name = form.cleaned_data.get("last_name")
            user.role = form.cleaned_data.get("role")
            user.save()

            messages.success(request, 'Користувача створено')
            return redirect('/users/list')
    data['form'] = form
    return render(request, 'app/useus/user_create.html', data)

@login_required
def home(request):
    return render(request, 'app/useus/home.html')



@login_required
def change_password(request):

    if request.method == 'POST':
        user =  request.user
        old_password = request.POST.get('old_password')
        new_password = request.POST.get('password1')
        confirm_password = request.POST.get('password2')
        if new_password == confirm_password:
            if check_password(old_password, user.password):
                user.set_password(new_password)
                user.save()
                login(request, user)
                messages.success(request, 'Пароль змінено')
            else:
                messages.warning(request, 'Старий пароль введено невірно!')
        else:
            messages.warning(request, 'Нові паролі не співпадають!')

    else:
        messages.warning(request, 'Метод не підтримується!')

    return redirect('settings')

@login_required
def user_logout(request):
    logout(request)
    return redirect('/accounts/login/')