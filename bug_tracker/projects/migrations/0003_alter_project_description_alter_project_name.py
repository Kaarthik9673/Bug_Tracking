# Generated by Django 4.0.2 on 2022-06-07 09:43

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0002_alter_project_options_project_description_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='description',
            field=models.TextField(max_length=1000, validators=[django.core.validators.MinLengthValidator(2)], verbose_name='Description'),
        ),
        migrations.AlterField(
            model_name='project',
            name='name',
            field=models.CharField(max_length=200, validators=[django.core.validators.MinLengthValidator(2)], verbose_name='Name'),
        ),
    ]
