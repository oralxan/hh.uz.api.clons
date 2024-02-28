from django.contrib.admin import *
from .models import Vacancy
@register(Vacancy)
class VacancyAdmin(ModelAdmin):
    list_display = ('id','title','company','created_date')
    list_display_links = ('id','title','company','created_date')
    ordering = ('created_date',)

# Register your models here.
