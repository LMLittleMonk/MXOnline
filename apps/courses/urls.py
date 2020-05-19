from apps.courses.views import CourseView,CourseDetailView,CourseLessonView,CourseCommentView
from django.conf.urls import url




urlpatterns = [
    url('^list/$',CourseView.as_view(),name='list'),
    url(r'^course(?P<course_id>\d+)/$', CourseDetailView.as_view(), name='detail'),
    url(r'^course(?P<course_id>\d+)/lesson/$', CourseLessonView.as_view(), name='lesson'),
    url(r'^course(?P<course_id>\d+)/comment/$', CourseCommentView.as_view(), name='comment'),
]
