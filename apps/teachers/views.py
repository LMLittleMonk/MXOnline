from django.shortcuts import render
from apps.organizations.models import Teacher
from django.views import View
from pure_pagination import PageNotAnInteger,Paginator,EmptyPage
from apps.operations.models import UserFavorite
from django.http import HttpResponseRedirect
from django.urls import reverse
# Create your views here.

class TeacherListView(View):
    def get(self,request,*args,**kwargs):

        teachers = Teacher.objects.all()
        fav_teachers = teachers.order_by('-fav_nums')[:3]
        sort = request.GET.get('sort','')
        if sort == 'hot':
            teachers=teachers.order_by('-fav_nums')

        try:
            page = request.GET.get('page', 1)
        except PageNotAnInteger:
            page = 1
        p = Paginator(teachers, per_page=3, request=request)  # 每页显示多少个
        all_teachers = p.page(page)

        return render(request,'teachers-list.html',{

            'all_teachers':all_teachers,
            'teachers':teachers,
            'fav_teachers':fav_teachers,
            'sort':sort,

        })


class TeacherDetailView(View):

    def get(self,request,id,*args,**kwargs):
        teacher = Teacher.objects.get(id=int(id))
        fav_teachers = teacher.org.teacher_set.order_by('-fav_nums')
        teacher.click_nums += 1
        teacher.save()
        has_fav_teacher = False
        has_fav_org = False
        if request.user.is_authenticated:
            # 查询用户是否收藏了该课程和机构 fav_type=1证明是课程收藏，如果有，证明用户收藏了这个课
            if UserFavorite.objects.filter(user=request.user, fav_id=teacher.id, fav_type=3):
                has_fav_teacher = True
            if UserFavorite.objects.filter(user=request.user, fav_id=teacher.org.id, fav_type=2):
                has_fav_org = True

        return render(request,'teacher-detail.html',{
            'teacher':teacher,
            'fav_teachers':fav_teachers,
            'has_fav_org':has_fav_org,
            'has_fav_teacher':has_fav_teacher,
        })

