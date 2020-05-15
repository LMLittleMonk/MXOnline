from apps.operations.views import AddFavView
from django.conf.urls import url




urlpatterns = [
    url('^fav/$',AddFavView.as_view(),name='fav'),
]
