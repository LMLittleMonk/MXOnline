from apps.operations.views import AddFavView,DeleteFavView
from django.conf.urls import url




urlpatterns = [
    url('^fav/$',AddFavView.as_view(),name='fav'),
    url('^(?P<fav_id>\d+)/$',DeleteFavView.as_view(),name='delete'),
]
