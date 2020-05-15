from django.shortcuts import render
from apps.operations.form import UserFavForm
from django.views import View
from django.http import JsonResponse
from apps.operations.models import UserFavorite
from apps.courses.models import Course,CourseOrg,Teacher


class AddFavView(View):
    """
    用户收藏实现
    """
    # 先判断用户是否登录
    def post(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return JsonResponse({
                "status":"fail",
                "msg": "用户未登录"
            })
        use_fav_form = UserFavForm(request.POST)
        if use_fav_form.is_valid():
            fav_id = use_fav_form.cleaned_data["fav_id"]
            fav_type = use_fav_form.cleaned_data["fav_type"]
            # 判断用户是否已经收藏
            existed_records = UserFavorite.objects.filter(user=request.user,fav_id=fav_id,fav_type=fav_type )
            if existed_records:
                # 收藏这条信息删除
                existed_records.delete()
                if fav_type == 1:
                    course = Course.objects.get(id = fav_id)
                    course.fav_nums -= 1
                    course.save()
                elif fav_type == 2:
                    cousre = Course.objects.get(id = fav_id)
                    course_org = cousre.course_org
                    course_org.org_collect -= 1
                    course_org.save()

                elif fav_type == 3:
                    teacher =Teacher.objects.get(id=fav_id)
                    teacher.fav_nums -= 1
                    teacher.save()
                return JsonResponse(
                    { "status":"success",
                    "msg": "收藏"}
                )
            else:
                user_fav = UserFavorite()
                user_fav.fav_id = fav_id
                user_fav.fav_type = fav_type
                user_fav.user = request.user
                user_fav.save()
                if fav_type == 1:
                    course = Course.objects.get(id = fav_id)
                    course.fav_nums += 1
                    course.save()
                elif fav_type == 2:
                    cousre = Course.objects.get(id = fav_id)
                    course_org = cousre.course_org
                    course_org.org_collect += 1
                    course_org.save()

                elif fav_type == 3:
                    teacher =Teacher.objects.get(id=fav_id)
                    teacher.fav_nums += 1
                    teacher.save()
                return JsonResponse(
                    {"status": "success",
                     "msg": "已收藏"}
                )

        else:
            return JsonResponse(
                {"status": "fail",
                 "msg": "参数错误"}
            )



