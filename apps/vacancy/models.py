from django.db.models import *
from apps.employer.models import Employer
from apps.employe.models import EmployeSkill
class Vacancy(Model):
    company = OneToOneField(
        Employer,
        verbose_name='Company',
        on_delete=CASCADE
    )
    title = CharField(
        'Tirle of the vacancy',
        max_length=256
    )
    salary_from = PositiveIntegerField(
        'Salary starts from (USD)'
    )
    salary_to = PositiveBigIntegerField(
        'Salary ends in(USD)'
    )
    description =TextField(
        'description of the vacancy'
    )
    required_skills = ManyToManyField(
        EmployeSkill,
        verbose_name='Required_skills'
    )
    created_date = DateTimeField(
        auto_now_add=True,
        verbose_name='vacancy pub'
    )
    class Meta:
        verbose_name = 'Vacancy'
        verbose_name_plural = 'Vacancies'
