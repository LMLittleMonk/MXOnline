from django.shortcuts import render
from django.views.generic import View
from apps.courses.models import *
from pure_pagination import Paginator, EmptyPage, PageNotAnInteger
from apps.operations.models import UserFavorite,CourseComments
from django.contrib.auth.mixins import LoginRequiredMixin
from apps.operations.models import UserCourse

class CourseView(View):
    def get(self,request,*args,**kwargs):
        user = request.user
        course = Course.objects.order_by('-add_time')
        hot_courses = Course.objects.order_by('-click_nums')[:2]
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
            'user':user
        })


class CourseDetailView(View):
    def get(self, request, course_id, *args, **kwargs):
        """
        获取课程详情页
        :param request:
        :param args:
        :param kwargs:
        :return:
        """
        # 根据id查询课程


        course = Course.objects.get(id=int(course_id))
        tags = course.coursetag_set.all()
        # 遍历
        tag_list = [tag.tag for tag in tags]
        course_tags = CourseTag.objects.filter(tag__in=tag_list).exclude(course__id=course.id)
        courses = set()
        for course_tag in course_tags:
            courses.add(course_tag.course)



        org = course.course_org
        lessons = course.lesson_set.all()
        teachers_nums = org.teacher_set.all().count()

        # 点击到课程 的详情就记录一次点击数
        course.click_nums += 1
        course.save()
        # 获取收藏状态
        has_fav_course = False
        has_fav_org = False
        if request.user.is_authenticated:
            # 查询用户是否收藏了该课程和机构 fav_type=1证明是课程收藏，如果有，证明用户收藏了这个课
            if UserFavorite.objects.filter(user=request.user, fav_id=course.id, fav_type=1):
                has_fav_course = True
            if UserFavorite.objects.filter(user=request.user, fav_id=course.course_org.id, fav_type=2):
                has_fav_org = True

        return render(request, 'course-detail.html',
                      {"course":course,
                       "has_fav_course":has_fav_course,
                       "has_fav_org":has_fav_org,
                       "org":org,
                       'teachers_nums':teachers_nums,
                       'lessons':lessons,
                       'courses':courses
                    })


class CourseLessonView(LoginRequiredMixin,View):
    login_url = '/login/'
    def get(self, request, course_id, *args, **kwargs):

        course = Course.objects.get(id=int(course_id))
        user_courses = UserCourse.objects.filter(course=course)
        user_ids = [user_course.user.id for user_course in user_courses]
        all_courses = UserCourse.objects.filter(user_id__in=user_ids).exclude(id=course_id)
        item = []
        for all_course in all_courses:
            item.append(all_course.course)


        return render(request,'course-video.html',{
            'course':course,

            'item':item
        })

class CourseCommentView(View):
    login_url = '/login/'

    def get(self, request, course_id, *args, **kwargs):
        course = Course.objects.get(id=int(course_id))
        comment = CourseComments.objects.filter(course=course)
        user_courses = UserCourse.objects.filter(course=course)
        user_ids = [user_course.user.id for user_course in user_courses]
        all_courses = UserCourse.objects.filter(user_id__in=user_ids).exclude(id=course_id)
        item = []
        for all_course in all_courses:
            item.append(all_course.course)

        fav_courses = Course.objects.exclude(id=int(course_id)).order_by('-fav_nums')[:3]
        return render(request, 'course-comment.html', {
            'course': course,
            'fav_courses': fav_courses,
            'item': item,
            'comments':comment
        })

class CoursePlayView(View):
    def get(self, request, lesson_id,video_id,*args, **kwargs):
        video = Video.objects.get(id = int(video_id),lesson_id = int(lesson_id))
        course = video.lesson.course
        user_courses = UserCourse.objects.filter(course=course)
        user_ids = [user_course.user.id for user_course in user_courses]
        all_courses = UserCourse.objects.filter(user_id__in=user_ids).exclude(id=course.id)
        item = []
        for all_course in all_courses:
            item.append(all_course.course)
        return render(request,'course-play.html',{
            'video':video,
            'course':course,
            'item':item
        })