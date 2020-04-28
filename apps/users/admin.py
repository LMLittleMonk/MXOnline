from django.contrib import admin

# Register your models here.

# class UserProfileAdmin(admin.ModelAdmin):
#     pass
# admin.site.register(UserProfile, UserProfileAdmin)
from django.contrib.auth.admin import UserAdmin
from apps.users.models import UserProfile
admin.site.register(UserProfile,UserAdmin)