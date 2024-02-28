from django.contrib.admin import *


from .models import Employer
@register(Employer)
class EmployerAdmin(ModelAdmin):
    list_display = ('id','name','city')
    list_display_links =  ('id','name','city')
    ordering = ('name',)