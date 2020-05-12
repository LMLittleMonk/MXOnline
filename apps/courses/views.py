from django.shortcuts import render
from django.views.generic import View
from apps.courses.models import *
from pure_pagination import Paginator, EmptyPage, PageNotAnInteger

class CourseView(View):
    def get(self,request,*args,**kwargs):
        course = Course.objects.order_by('-add_time')
        hot_courses = Course.objects.order_by('-click_nums')[:3]
        sort = request.GET.get('sort',"")
        if sort == 'hot':
            course = course.order_by('-click_nums')
        elif sort == 'students':
            course = course.order_by('-students')
        try:
            page = request.GET.get('page', 1)
        except PageNotAnInteger:
            page = 1
        p = Paginator(course, per_page=3, request=request)  # 每页显示多少个
        courses = p.page(page)
        return render(request,'course-list.html',{
            'courses':courses,
            'sort':sort,
            'hot_courses':hot_courses,
        })