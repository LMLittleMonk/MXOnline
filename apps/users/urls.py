from apps.users.views import UserInfoView,UserCourseView,UserImgUploadView,FavCourseView,FavOrgView,FavTeacherView,UserMsgView,UserChangeView
from django.conf.urls import url

urlpatterns = [
    url('^detail/$',UserInfoView.as_view(),name='detail'),
    url('^mycourse/$',UserCourseView.as_view(),name='mycourse'),
    url('^favcourse/$',FavCourseView.as_view(),name='favcourse'),
    url('^favteacher/$',FavTeacherView.as_view(),name='favteacher'),
    url('^favorg/$',FavOrgView.as_view(),name='favorg'),
    url('^msg/$',UserMsgView.as_view(),name='msg'),

    url('^upload/$',UserImgUploadView.as_view(),name='upload'),
    url('^xiugai/$',UserChangeView.as_view(),name='xiugai')



]
