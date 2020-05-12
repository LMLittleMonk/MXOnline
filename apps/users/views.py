from django.shortcuts import render
from django.views.generic.base import View
# Create your views here.
from apps.users.models import *
from apps.users.form import *
from django.urls import reverse
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib.auth import authenticate,login

def IndexView(request):
    return render(request,'index.html')

class LoginView(View):
    def get(slef,request,*args,**kwargs):
        return render(request,'login.html')
    def post(self,request,*args,**kwargs):
        loginform = LoginForm(request.POST)
        if loginform.is_valid():
            username = loginform.cleaned_data["username"]
            password = loginform.cleaned_data["password"]
            user = authenticate(username=username,password=password)
            if user is not None:
                login(request,user)
                return HttpResponseRedirect(reverse("index"))
            else:
                return render(request,'login.html',{'msg':'用户名或密码错误','loginform':loginform})
        else:
            return render(request,'login.html',{'loginform':loginform})