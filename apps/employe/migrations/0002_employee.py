# Generated by Django 4.2.8 on 2024-02-28 18:38

from django.db import migrations, models
import image_optimizer.fields


class Migration(migrations.Migration):

    dependencies = [
        ('employe', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fullname', models.CharField(max_length=128, verbose_name='Fullname')),
                ('about', models.TextField(verbose_name='About the employee')),
                ('experience', models.PositiveSmallIntegerField(verbose_name='Experience in years')),
                ('email', models.EmailField(max_length=254, verbose_name='email')),
                ('number', models.CharField(max_length=13, verbose_name='phone number')),
                ('photo', image_optimizer.fields.OptimizedImageField(upload_to='employee-photos/%Y/%m/%d', verbose_name='Employee photo')),
                ('skills', models.ManyToManyField(to='employe.employeskill', verbose_name='Skills')),
            ],
            options={
                'verbose_name': 'Employee',
                'verbose_name_plural': 'Employees',
            },
        ),
    ]
