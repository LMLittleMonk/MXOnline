from apps.teachers.views import TeacherListView
from django.conf.urls import url




urlpatterns = [
    url('^list/$',TeacherListView.as_view(),name='list'),
]
