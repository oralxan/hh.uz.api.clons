from django.db.models import *
from image_optimizer.fields import OptimizedImageField
class EmployeSkill(Model):
    name = CharField(
        'Skill',
        max_length=64
    )
    def __str__(self):
        return f'{self.name}'
    class Meta:
        verbose_name = 'EmployeSkill'
        verbose_name_plural = 'EmployeSkills'

class Employee(Model):
    fullname = CharField(
        'Fullname',
        max_length=128
    )
    about = TextField(
        'About the employee'

    )
    experience = PositiveSmallIntegerField(
        'Experience in years'
    )
    skills= ManyToManyField(
        EmployeSkill,
        verbose_name='Skills'
    )
    email =EmailField(
        'email'
    )
    number = CharField(
        'phone number',
        max_length=13
    )
    photo = OptimizedImageField(
        verbose_name = 'Employee photo',
        upload_to = 'employee-photos/%Y/%m/%d',
        optimized_image_output_size=(50, 50),
        optimized_image_resize_method='cover'
    )
    class Meta:
        verbose_name = 'Employee'
        verbose_name_plural = 'Employees'
