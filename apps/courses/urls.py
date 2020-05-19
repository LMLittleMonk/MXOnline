from apps.courses.views import CourseView,CourseDetailView,CourseLessonView,CourseCommentView,CoursePlayView
from django.conf.urls import url




urlpatterns = [
    url('^list/$',CourseView.as_view(),name='list'),
    url(r'^course(?P<course_id>\d+)/$', CourseDetailView.as_view(), name='detail'),
    url(r'^course(?P<course_id>\d+)/lesson/$', CourseLessonView.as_view(), name='lesson'),
    url(r'^course(?P<course_id>\d+)/comment/$', CourseCommentView.as_view(), name='comment'),
    url(r'^lesson(?P<lesson_id>\d+)/video(?P<video_id>\d+)/$', CoursePlayView.as_view(), name='video'),
]
