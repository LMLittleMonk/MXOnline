from apps.teachers.views import TeacherListView,TeacherDetailView
from django.conf.urls import url




urlpatterns = [

    url(r'^list/$',TeacherListView.as_view(),name='list'),
    url(r'^detail(?P<id>\d+)/$', TeacherDetailView.as_view(), name='detail'),


]
