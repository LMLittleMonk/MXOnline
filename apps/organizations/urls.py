from apps.organizations.views import OrgView,AddAsk,OrgDetailHomeView,OrgDetailCourseView,OrgDetailView,TeacherView
from django.conf.urls import url

urlpatterns = [
    url('^list/$',OrgView.as_view(),name='list'),
    url('^add_ask/$',AddAsk.as_view(),name='add_ask'),
    url(r'^org(?P<org_id>\d+)/homepage/$', OrgDetailHomeView.as_view(), name='homepage'),
    url(r'^org(?P<org_id>\d+)/detail/$', OrgDetailView.as_view(), name='detail'),
    url(r'^org(?P<org_id>\d+)/teachers/$', TeacherView.as_view(), name='teachers'),
    url(r'^org(?P<course_org_id>\d+)/courselist/$', OrgDetailCourseView.as_view(), name='courselist')

]
