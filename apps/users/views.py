from django.shortcuts import render
from django.views.generic.base import View
from apps.users.models import *
from apps.users.form import LoginForm,RegisterForm,ImageUploadForm
from django.urls import reverse
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.hashers import make_password
from apps.operations.models import UserFavorite
from apps.courses.models import Course,CourseOrg,Teacher




def IndexView(request):

    return render(request,'index.html')



class LoginView(View):

    def get(slef,request,*args,**kwargs):

        if request.user.is_authenticated:
            return HttpResponseRedirect(reverse("index"))
        next = request.GET.get("next", "")

        return render(request, 'login.html', {"next": next})

    def post(self,request,*args,**kwargs):

        loginform = LoginForm(request.POST)

        if loginform.is_valid():
            username = loginform.cleaned_data["username"]
            password = loginform.cleaned_data["password"]
            user = authenticate(username=username,password=password)

            if user is not None:
                login(request,user)
                next = request.GET.get("next", "")
                if next:
                    return HttpResponseRedirect(next)

                return HttpResponseRedirect(reverse("index"))
            else:
                return render(request,'login.html',{'msg':'用户名或密码错误','loginform':loginform})
        else:
            return render(request,'login.html',{'loginform':loginform})




class LogoutView(View):

    def get(slef,request,*args,**kwargs):
        logout(request)
        return HttpResponseRedirect(reverse("index"))




class RegisterView(View):
    def get(slef,request,*args,**kwargs):
        return render(request,'register.html')
    def post(self,request,*args,**kwargs):
        registerform = RegisterForm(request.POST)
        if registerform.is_valid():
            username = registerform.cleaned_data["username"]
            password = registerform.cleaned_data["password"]
            email = registerform.cleaned_data["email"]
            user = UserProfile.objects.filter(username=username)
            if user:
                return render(request, 'register.html', {'msg': '用户名重复请换一个用户名', 'registerform': registerform})
            else:
                password = make_password(password)
                user1 = UserProfile.objects.create(username=username,password=password,email=email)
                user1.save()
                login(request,user1)
                return render(request,'index.html')
        else:
            return render(request, 'register.html', {'msg': '用户名或密码错误', 'registerform': registerform})



class UserInfoView(View):
    def get(self,request,*args,**kwargs):
        return render(request,'usercenter-info.html')



class UserImgUploadView(View):
    def post(self,request,*args,**kwargs):
        image = ImageUploadForm(request.POST,request.FILES)
        if image.is_valid():
            request.user.save()

            return render(request, 'usercenter-info.html')
        else:
            return render(request, 'usercenter-info.html')




class UserCourseView(View):
    def get(self,request,*args,**kwargs):
        return render(request,'usercenter-mycourse.html',{
        })


class FavCourseView(View):
    def get(self,request,*args,**kwargs):
        userfavs = UserFavorite.objects.filter(user_id=request.user.id,fav_type=1)
        if userfavs:
            list = [course.fav_id for course in userfavs]
            courses = Course.objects.filter(id__in = list)

            return render(request,'usercenter-fav-course.html',{
                'fav_course':courses,
                'isexist':True
            })
        else:
            return render(request,'usercenter-fav-course.html',{
                'isexist': False
            })

class FavOrgView(View):
    def get(self,request,*args,**kwargs):
        userfavs = UserFavorite.objects.filter(user_id=request.user.id,fav_type=2)
        if userfavs:
            list = [org.fav_id for org in userfavs]
            orgs = CourseOrg.objects.filter(id__in = list)

            return render(request,'usercenter-fav-org.html',{
                'fav_orgs':orgs,
                'isexist':True
            })

        else:

            return render(request,'usercenter-fav-org.html',{
                'isexist': False
            })




class FavTeacherView(View):
    def get(self,request,*args,**kwargs):
        userfavs = UserFavorite.objects.filter(user_id=request.user.id,fav_type=3)
        if userfavs:
            list = [teacher.fav_id for teacher in userfavs]
            teachers = Teacher.objects.filter(id__in = list)

            return render(request,'usercenter-fav-teacher.html',{
                'fav_teachers':teachers,
                'isexist':True
            })

        else:

            return render(request,'usercenter-fav-teacher.html',{
                'isexist': False
            })

