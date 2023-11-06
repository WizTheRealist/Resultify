import datetime

from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.urls import reverse_lazy
from django.views import generic

from RESULTIFYAPP.EmailBackEnd import EmailBackEnd
from django.shortcuts import render, redirect
from .forms import SignUpForm

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('login')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})

def showDemoPage(request):
    return render(request,"demo.html")

def ShowLoginPage(request):
    return render(request,"login_page.html")

def doLogin(request):
    if request.method!="POST":
        return HttpResponse("<h2>Method Not Allowed</h2>")
    else:
        user = EmailBackEnd.authenticate(request, request.POST.get("email"), password=request.POST.get("password"))
        if user!=None:
           login(request,user)
           if user.user_type == "1":
                return HttpResponseRedirect('/admin_home')
           elif user.user_type=="2":
                return HttpResponseRedirect(reverse("staff_home"))
           else:
                return HttpResponseRedirect(reverse("student_home"))
           #return HttpResponseRedirect('/admin_home')
        else:
            return HttpResponse("Invalid Login Details")



def GetUserDetails(request):
    if request.user!=None:
        return HttpResponse("User : "+request.user.email+" usertype : "+str(request.user.user_type))
    else:
        return HttpResponse("Please Login First")

def logout_user(request):
    logout(request)
    return HttpResponseRedirect("/")