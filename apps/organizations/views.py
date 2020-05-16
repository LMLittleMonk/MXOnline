from django.shortcuts import render
from django.views.generic import View
from apps.organizations.models import CourseOrg, City, Teacher
from pure_pagination import Paginator, EmptyPage, PageNotAnInteger
from apps.organizations.form import AddAskForm
from django.http import JsonResponse
from apps.users.models import UserProfile


# Create your views here.
class OrgView(View):
    def get(self, request, *args, **kwargs):
        """
        展示授课机构列表页
        :param request:
        :param args:
        :param kwargs:
        :return:
        """
        user = request.user
        all_orgs = CourseOrg.objects.all()
        all_citys = City.objects.all()
        # 获取点击的类目
        category = request.GET.get("ct", "")
        if category:
            all_orgs = all_orgs.filter(org_type=category)

        # 对所在城市进行筛选
        city_id = request.GET.get('city', '0')
        if city_id != '0':
            if city_id.isdigit():
                all_orgs = all_orgs.filter(city_id=int(city_id))
        else:
            all_orgs = all_orgs.all()

        sort = request.GET.get('sort', '')
        if sort == 'students':
            all_orgs = all_orgs.order_by('-org_learners')
        elif sort == 'courses':
            all_orgs = all_orgs.order_by('-org_courses')

        org_nums = all_orgs.count()

        orgs_order = all_orgs.order_by('-org_collect')[0:3]

        try:
            page = request.GET.get('page', 1)
        except PageNotAnInteger:
            page = 1
        p = Paginator(all_orgs, per_page=5, request=request)  # 每页显示多少个
        orgs = p.page(page)
        return render(request, 'orglist.html',
                      {'city_id': int(city_id),
                       'all_orgs': orgs,
                       'org_nums': org_nums,
                       'all_citys': all_citys,
                       'category': category,
                       'sort': sort,
                       'orgs_order': orgs_order,
                       'user':user
                       })


class AddAsk(View):
    def post(self, request, *args, **kwargs):
        userask_form = AddAskForm(request.POST)
        if userask_form.is_valid():
            userask_form.save(commit=True)
            return JsonResponse({
                "status": "success",
                "msg": "提交成功"
            })
        else:
            return JsonResponse({
                "status": "fail",
                "msg": "添加出错"
            })


class OrgDetailHomeView(View):
    def get(self, request, org_id, *args, **kwargs):
        """
        获取课程详情页
        :param request:
        :param args:
        :param kwargs:
        :return:
        """
        # 根据id查询课程
        user = request.user
        org = CourseOrg.objects.get(id=int(org_id))
        # 点击到课程 的详情就记录一次点击数
        courses = org.course_set.all()
        teachers = org.teacher_set.all()
        org.org_click += 1
        org.save()
        # 获取收藏状态

        return render(request, 'org-detail-homepage.html',
                      {
                          "org": org,
                          'courses': courses,
                          'teachers': teachers,
                          'user':user
                      })


class OrgDetailCourseView(View):
    def get(self, request, course_org_id, *args, **kwargs):
        user = request.user
        org = CourseOrg.objects.get(id=int(course_org_id))
        all_courses = org.course_set.all()

        try:
            page = request.GET.get('page', 1)
        except PageNotAnInteger:
            page = 1
        p = Paginator(all_courses, per_page=1, request=request)  # 每页显示多少个
        courses = p.page(page)
        return render(request, 'org-detail-course.html',
                      {
                          "org": org,
                          'courses': courses,
                          'user':user
                      })



class OrgDetailView(View):
    def get(self, request, org_id, *args, **kwargs):
        org = CourseOrg.objects.get(id=int(org_id))
        user = request.user
        return render(request, 'org-detail-desc.html',
                      {
                          "org": org,
                          'user':user
                      })


class TeacherView(View):
    def get(self, request, org_id, *args, **kwargs):
        user = request.user
        org = CourseOrg.objects.get(id=int(org_id))
        teachers = org.teacher_set.all()
        try:
            page = request.GET.get('page', 1)
        except PageNotAnInteger:
            page = 1
        p = Paginator(teachers, per_page=1, request=request)  # 每页显示多少个
        teachers = p.page(page)
        return render(request, 'org-detail-teachers.html',
                      {
                          "org": org,
                          "teachers":teachers,
                          'user':user
                      })