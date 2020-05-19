from apps.users.views import UserInfoView,UserCourseView,UserImgUploadView,FavCourseView
from django.conf.urls import url

urlpatterns = [
    url('^detail/$',UserInfoView.as_view(),name='detail'),
    url('^mycourse/$',UserCourseView.as_view(),name='mycourse'),
    url('^favcourse/$',FavCourseView.as_view(),name='favcourse'),
    url('^upload/$',UserImgUploadView.as_view(),name='upload')



]
