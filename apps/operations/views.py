from django.shortcuts import render
from apps.operations.form import UserFavForm
from django.views import View
from django.http import JsonResponse,HttpResponse,HttpResponseRedirect
from apps.operations.models import UserFavorite
from apps.courses.models import Course,CourseOrg,Teacher
from PIL import Image, ImageDraw, ImageFont
from django.utils.six import BytesIO
from django.urls import reverse

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
                    org = CourseOrg.objects.get(id = fav_id)
                    org.org_collect -= 1
                    org.save()

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
                    org = CourseOrg.objects.get(id = fav_id)
                    org.org_collect += 1
                    org.save()

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


class DeleteFavView(View):
    def get(self,request,fav_id,*args,**kwargs):
        userfav = UserFavorite.objects.filter(fav_id=int(fav_id),fav_type=1,user_id=request.user.id)
        userfav.delete()
        return HttpResponseRedirect(reverse('user:favcourse'))

def verify_code(request):
    #引入随机函数模块
    import random
    #定义变量，用于画面的背景色、宽、高
    bgcolor = (random.randrange(20, 100), random.randrange(
        20, 100), 255)
    width = 100
    height = 35
    #创建画面对象
    im = Image.new('RGB', (width, height), bgcolor)
    #创建画笔对象
    draw = ImageDraw.Draw(im)
    #调用画笔的point()函数绘制噪点
    for i in range(0, 100):
        xy = (random.randrange(0, width), random.randrange(0, height))
        fill = (random.randrange(0, 255), 255, random.randrange(0, 255))
        draw.point(xy, fill=fill)
    #定义验证码的备选值
    str1 = 'ABCD123EFGHIJK456LMNOPQRS789TUVWXYZ0'
    #随机选取4个值作为验证码
    rand_str = ''
    for i in range(0, 4):
        rand_str += str1[random.randrange(0, len(str1))]
    #构造字体对象，ubuntu的字体路径为“C:/windows/Fonts”
    font = ImageFont.truetype('arial.ttf', 36)
    #构造字体颜色
    fontcolor = (255, random.randrange(0, 255), random.randrange(0, 255))
    #绘制4个字
    draw.text((5, 2), rand_str[0], font=font, fill=fontcolor)
    draw.text((25, 2), rand_str[1], font=font, fill=fontcolor)
    draw.text((50, 2), rand_str[2], font=font, fill=fontcolor)
    draw.text((75, 2), rand_str[3], font=font, fill=fontcolor)
    #释放画笔
    del draw
    #存入session，用于做进一步验证
    request.session['verifycode'] = rand_str
    #内存文件操作
    buf = BytesIO()
    #将图片保存在内存中，文件类型为png
    im.save(buf, 'png')
    #将内存中的图片数据返回给客户端，MIME类型为图片png
    return HttpResponse(buf.getvalue(), 'image/png')



