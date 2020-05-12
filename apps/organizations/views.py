from django.shortcuts import render
from django.views.generic import View
from apps.organizations.models import CourseOrg, City, Teacher
from pure_pagination import Paginator, EmptyPage, PageNotAnInteger
from apps.organizations.form import AddAskForm
from django.http import JsonResponse

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
        all_orgs = CourseOrg.objects.all()
        all_citys = City.objects.all()
        # 获取点击的类目
        category = request.GET.get("ct","")
        if category:
            all_orgs = all_orgs.filter(org_type=category)

        # 对所在城市进行筛选
        city_id = request.GET.get('city','0')
        if city_id != '0':
            if city_id.isdigit():
                all_orgs = all_orgs.filter(city_id=int(city_id))
        else:
            all_orgs = all_orgs.all()

        sort = request.GET.get('sort','')
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
        p = Paginator(all_orgs,per_page=5, request=request) # 每页显示多少个
        orgs = p.page(page)
        return render(request, 'orglist.html',
                      {'city_id':int(city_id),
                       'all_orgs':orgs,
                       'org_nums':org_nums,
                       'all_citys':all_citys,
                       'category':category,
                       'sort':sort,
                       'orgs_order':orgs_order,
                       })
class AddAsk(View):
    def post(self, request, *args, **kwargs):
        userask_form = AddAskForm(request.POST)
        if userask_form.is_valid():
            userask_form.save(commit=True)
            return JsonResponse({
                "status":"success",
                "msg":"提交成功"
            })
        else:
            return JsonResponse({
                "status": "fail",
                "msg": "添加出错"
            })
