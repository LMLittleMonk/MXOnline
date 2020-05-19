from apps.operations.views import AddFavView,DeleteFavView,DeleteOrgView,DeleteTeacherView
from django.conf.urls import url




urlpatterns = [
    url('^fav/$',AddFavView.as_view(),name='fav'),
    url('^course(?P<fav_id>\d+)/$',DeleteFavView.as_view(),name='deletecourse'),
    url('^org(?P<fav_id>\d+)/$',DeleteOrgView.as_view(),name='deleteorg'),
    url('^teacher(?P<fav_id>\d+)/$',DeleteTeacherView.as_view(),name='deleteteacher'),
]
