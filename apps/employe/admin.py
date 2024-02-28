from django.contrib.admin import *
from .models import (
    EmployeSkill,
    Employee
    )
@register(EmployeSkill)
class EmployeSkillAdmin(ModelAdmin):
    list_display = ('id','name')
    list_display_links = ('id','name')
    ordering = ('name',)
@register(Employee)
class EmployeeAdmin(ModelAdmin):
    list_display = ('id','fullname')
    list_display_links = ('id','fullname')
    ordering = ('fullname',)