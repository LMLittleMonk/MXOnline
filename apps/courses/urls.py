from apps.courses.views import CourseView
from django.conf.urls import url

urlpatterns = [
    url('^list/$',CourseView.as_view(),name='list'),
]
