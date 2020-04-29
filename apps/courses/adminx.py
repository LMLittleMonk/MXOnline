import xadmin
from apps.courses.models import Course

class CourseAdmin(object):
    # 显示字典
    list_display = ["id", "name", "desc","learn_times", "degree"]
    # 搜索字段
    search_fields = ["name", "desc"]
    list_filter = ["id", "name", "desc","learn_times", "degree"]

xadmin.site.register(Course, CourseAdmin)