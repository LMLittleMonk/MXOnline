from django.db import models
from apps.users.models import UserProfile
from apps.users.models import BaseModel
# Create your models here.

class City(BaseModel):
    cname = models.CharField(verbose_name="城市名称",max_length=20)
    desc = models.CharField(verbose_name="城市描述",max_length=300)
    class Meta:
        verbose_name = "城市信息"
        verbose_name_plural = verbose_name
    def __str__(self):
        return self.cname

class CourseOrg(BaseModel):
    org_name = models.CharField(verbose_name="机构名称",max_length=20)
    org_label = models.CharField(verbose_name="机构标签",max_length=30)
    org_type = models.CharField(verbose_name="机构类别",choices=(("pxjg","培训机构"),("gr", "个人"), ("gx", "高校")),max_length=4)
    org_click = models.IntegerField(verbose_name="点击数",default=0)
    org_collect = models.IntegerField(verbose_name="收藏数",default=0)
    org_image = models.ImageField(upload_to="org/%Y/%m",verbose_name="logo", max_length=100)
    org_location = models.CharField(verbose_name="机构地址",max_length=300)
    org_learners = models.IntegerField(verbose_name="学习人数",default=0)
    org_courses = models.IntegerField(verbose_name="课程数",default=0)
    org_isauth = models.BooleanField(default=False,verbose_name="是否认证")
    org_ismedal = models.BooleanField(default=False,verbose_name="是否金牌")
    city = models.ForeignKey(City, on_delete=models.CASCADE, verbose_name="所在城市")
    class Meta:
        verbose_name = "机构信息"
        verbose_name_plural = verbose_name
    def __str__(self):
        return self.org_name
    def courses(self):
        courses = self.course_set.filter(is_classics=True)[:3]
        return courses


class Teacher(BaseModel):
    user = models.OneToOneField(UserProfile, on_delete=models.SET_NULL, null=True, blank=True,verbose_name="用户")
    org = models.ForeignKey(CourseOrg, on_delete=models.CASCADE, verbose_name="所属机构")
    name = models.CharField(max_length=50, verbose_name="教师名",default="")
    work_years = models.IntegerField(default=0, verbose_name="工作年限")
    work_company = models.CharField(max_length=50, verbose_name="就职公司",default="")
    work_position = models.CharField(max_length=50, verbose_name="公司职位",default="")
    points = models.CharField(max_length=50, verbose_name="教学特点",default="好")
    click_nums = models.IntegerField(default=0, verbose_name="点击数")
    fav_nums = models.IntegerField(default=0, verbose_name="收藏数")
    age = models.IntegerField(default=18, verbose_name="年龄")
    image = models.ImageField(upload_to="teacher/%Y/%m", verbose_name="头像", max_length=100)

    class Meta:
        verbose_name = "教师"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name

    def course_nums(self):
        return self.course_set.all().count()
