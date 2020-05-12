from apps.organizations.views import OrgView,AddAsk
from django.conf.urls import url

urlpatterns = [
    url('^list/$',OrgView.as_view(),name='list'),
    url('^add_ask/$',AddAsk.as_view(),name='add_ask')
]
