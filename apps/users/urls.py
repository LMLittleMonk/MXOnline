from apps.users.views import UserInfoView
from django.conf.urls import url

urlpatterns = [
    url('^detail/$',UserInfoView.as_view(),name='detail'),


]
