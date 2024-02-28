from django.db.models import *
from image_optimizer.fields import OptimizedImageField


class Employer(Model):
    name = CharField(
        'Employer name',
        max_length=256
    )
    about = TextField(
        'About employer',
        blank=True,
        null=True
    )
    foundation_date = PositiveSmallIntegerField(
        'foundation of the company'
    )
    email = EmailField(
        'email of company'
    )
    number = CharField(
        'number',
        max_length=13
    )
    company_photo = OptimizedImageField(
        verbose_name ='company photo',
        upload_to='emplyer-photos/%Y/%m/%d',
        optimized_image_output_size=(500, 500),
        optimized_image_resize_method='cover'
    )
    city = CharField(
        'Location of yhe city',
        max_length=64
    )
    def __str__(self) :
        return f'{self.name}'
    class Meta:
        verbose_name = 'Employer'
        verbose_name_plural = 'Employers'