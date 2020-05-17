from django.shortcuts import render
from apps.organizations.models import Teacher
from django.views import View
from pure_pagination import PageNotAnInteger,Paginator,EmptyPage
# Create your views here.

class TeacherListView(View):
    def get(self,request,*args,**kwargs):

        user =request.user
        all_teachers = Teacher.objects.all()
        fav_teachers = all_teachers.order_by('-fav_nums')[:3]
        sort = request.GET.get('sort','')
        if sort == 'hot':
            all_teachers=all_teachers.order_by('-fav_nums')

        try:
            page = request.GET.get('page', 1)
        except PageNotAnInteger:
            page = 1
        p = Paginator(all_teachers, per_page=1, request=request)  # 每页显示多少个
        teachers = p.page(page)

        return render(request,'teachers-list.html',{

            'all_teachers':teachers,
            'teachers':all_teachers,
            'fav_teachers':fav_teachers,
            'sort':sort,
            'user':user

        })


class TeacherDetailView(View):

    def get(self,request,id,*args,**kwargs):
        user = request.user
        teacher = Teacher.objects.get(id=int(id))
        fav_teachers = teacher.org.teacher_set.order_by('-fav_nums')

        return render(request,'teacher-detail.html',{
            'teacher':teacher,
            'user':user,
            'fav_teachers':fav_teachers
        })
