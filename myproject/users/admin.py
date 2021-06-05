from django.contrib import admin
from django.contrib.auth.admin import GroupAdmin, UserAdmin
from django.contrib.auth.models import Group, User

# Register your models here.

from .models import Role, Member

admin.site.unregister(Group)
admin.site.register(Role, GroupAdmin)
admin.site.register(Member)
# admin.site.register(CustomUser)
