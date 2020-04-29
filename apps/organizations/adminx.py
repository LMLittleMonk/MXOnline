import xadmin
from apps.organizations.models import *

class CityAdmin(object):
    # 显示字典
    list_display = ["id", "cname", "desc"]
    # 搜索字段
    search_fields = ["id", "cname"]

xadmin.site.register(City, CityAdmin)

class OrganizationAdmin(object):
    # 显示字典
    list_display = ["id", "org_name", "org_label","org_type", "org_click","org_collect","org_location"]
    # 搜索字段
    search_fields = ["org_name", "id" ,"org_label", "org_click","org_collect","org_location"]

xadmin.site.register(CourseOrg, OrganizationAdmin)

class TeacherAdmin(object):
    # 显示字典
    list_display = ["id", "tea_name","tea_org","tea_workyears","tea_company","tea_position","tea_features","tea_age"]
    # 搜索字段
    search_fields = ["id", "tea_name","tea_org","tea_workyears","tea_company","tea_position","tea_features"]

xadmin.site.register(Teacher, TeacherAdmin)