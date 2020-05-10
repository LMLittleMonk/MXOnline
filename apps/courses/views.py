from django.shortcuts import render
from django.views.generic import View
from apps.courses.models import *
from pure_pagination import Paginator, EmptyPage, PageNotAnInteger

class CourseView(View):
    def get(self,request,*args,**kwargs):
        course = Course.objects.all()
        try:
            page = request.GET.get('page', 1)
        except PageNotAnInteger:
            page = 1
        p = Paginator(course, per_page=1, request=request)  # 每页显示多少个
        courses = p.page(page)
        return render(request,'course-list.html',{'courses':courses})