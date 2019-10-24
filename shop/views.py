from django.shortcuts import render,redirect
from django.http import HttpResponse,HttpResponseRedirect
from .forms import LoginForm,RegisterForm
from django.contrib.auth import authenticate,login,logout
from .models import AdvUser
from django.core.exceptions import ValidationError
from new import settings

def index(request):

    return render(request,'shop/index.html')
def my_login(request):
    form_register = RegisterForm
    form_login = LoginForm
    if request.method == "POST":
        form_login = LoginForm(request.POST)
        if form_login.is_valid():
            usermail = form_login.cleaned_data['email1']
            password = form_login.cleaned_data['password1']
            user = authenticate(request,username=usermail,password=password)
            if user is not None:
                login(request,user)
                return HttpResponseRedirect(request.META.get('HTTP_REFERER','/'))
            else:
                return render(request, 'shop/registration/register.html', {'form_login': form_login,'form_register':form_register})
        else:
            return render(request, 'shop/registration/register.html', {'form_login': form_login,'form_register':form_register})
    return render(request, 'shop/registration/register.html',{'form_login': form_login, 'form_register': form_register})
def my_logout(request):
    logout(request)
    return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))
def my_register(request):
    form_register = RegisterForm
    form_login = LoginForm
    if request.method == 'POST':
       form = RegisterForm(request.POST)
       if form.is_valid():
           user = AdvUser.objects.create_user(email=form.cleaned_data['email'],
                                              password=form.cleaned_data['password'],
                                              password1=form.cleaned_data['password2'],
                                              first_name=form.cleaned_data['first_name'],
                                              last_name=form.cleaned_data['last_name']
                                              )
           username = form.cleaned_data.get('email')
           my_password = form.cleaned_data.get('password')
           user = authenticate(username=username, password=my_password)
           login(request, user)
           return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))
       else:
           return render(request, 'shop/registration/register.html',{'form_register':form,'form_login': form_login})
    return render(request,'shop/registration/register.html',{'form_register':form_register,'form_login': form_login})

