from apps.users.views import UserInfoView,UserCourseView
from django.conf.urls import url

urlpatterns = [
    url('^detail/$',UserInfoView.as_view(),name='detail'),
    url('^mycourse/$',UserCourseView.as_view(),name='mycourse'),


]
