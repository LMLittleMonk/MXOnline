import xadmin
from apps.organizations.models import *

class CityAdmin(object):
    # 显示字典
    list_display = ["id", "cname", "desc"]
    # 搜索字段
    search_fields = ["id", "cname"]



class OrganizationAdmin(object):
    # 显示字典
    list_display = ["id", "org_name", "org_label","org_type", "org_click","org_collect","org_location"]
    # 搜索字段
    search_fields = ["org_name", "id" ,"org_label", "org_click","org_collect","org_location"]


class TeacherAdmin(object):
    list_display = ['org', 'name', 'work_years', 'work_company']
    search_fields = ['org', 'name', 'work_years', 'work_company']
    list_filter = ['org', 'name', 'work_years', 'work_company']


xadmin.site.register(City, CityAdmin)
xadmin.site.register(CourseOrg, OrganizationAdmin)
xadmin.site.register(Teacher, TeacherAdmin)