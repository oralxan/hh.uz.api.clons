# Generated by Django 4.2.8 on 2024-02-28 18:13

from django.db import migrations, models
import image_optimizer.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256, verbose_name='Employer name')),
                ('about', models.TextField(blank=True, null=True, verbose_name='About employer')),
                ('foundation_date', models.PositiveSmallIntegerField(verbose_name='foundation of the company')),
                ('email', models.EmailField(max_length=254, verbose_name='email of company')),
                ('number', models.CharField(max_length=13, verbose_name='number')),
                ('company_photo', image_optimizer.fields.OptimizedImageField(upload_to='emplyer-photos/%Y/%m/%d', verbose_name='company photo')),
                ('city', models.CharField(max_length=64, verbose_name='Location of yhe city')),
            ],
            options={
                'verbose_name': 'Employer',
                'verbose_name_plural': 'Employers',
            },
        ),
    ]