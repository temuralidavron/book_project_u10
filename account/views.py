from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse
from django.shortcuts import render, redirect

from account.forms import RegisterForm, LoginForm


# Create your views here.
def register_user(request):
    if request.method=='POST':
        form=RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("login")
    else:
        form=RegisterForm()
    return render(request,"account/regitser.html",{'norm':form})


def login_user(request):
    if request.method=='POST':
        form=LoginForm(request.POST)
        if form.is_valid():
            username=form.cleaned_data.get('username')
            password=form.cleaned_data.get('password')
            user=authenticate(username=username,password=password)
            if user:
                login(request, user)

                return redirect("book-list")
            else:
                return HttpResponse("Xatolik booooor")
    else:
        form=LoginForm()
    return render(request,"account/login.html",{'norm':form})



def logout_user(request):
    logout(request)
    return redirect("login")