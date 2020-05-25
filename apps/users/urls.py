from apps.users.views import UserInfoView,UserCourseView,UserImgUploadView,FavCourseView,FavOrgView,FavTeacherView,UserMsgView,UserChangePwdView
from django.conf.urls import url



urlpatterns = [
    url('^detail/$',UserInfoView.as_view(),name='detail'),
    url('^mycourse/$',UserCourseView.as_view(),name='mycourse'),
    url('^favcourse/$',FavCourseView.as_view(),name='favcourse'),
    url('^favteacher/$',FavTeacherView.as_view(),name='favteacher'),
    url('^favorg/$',FavOrgView.as_view(),name='favorg'),
    url('^msg/$',UserMsgView.as_view(),name='msg'),
    # url(r'^mycourse/$',login_required(TemplateView.as_view(template_name='usercenter-mycourse.html'), login_url='/login/'),{"current_page": "mycourse"}, name='mycourse'),
    url('^upload/$',UserImgUploadView.as_view(),name='upload'),
    url('^update/pwd/$',UserChangePwdView.as_view(),name='update_pwd'),






]
