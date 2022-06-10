# Generated by Django 4.0.2 on 2022-06-08 12:57

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('projects', '0004_task'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='task',
            options={'ordering': ['start_time'], 'verbose_name': 'Task', 'verbose_name_plural': 'Tasks'},
        ),
        migrations.AlterField(
            model_name='task',
            name='end_time',
            field=models.DateTimeField(blank=True, null=True, verbose_name='End time'),
        ),
        migrations.AlterField(
            model_name='task',
            name='performer',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Performer'),
        ),
        migrations.AlterField(
            model_name='task',
            name='start_time',
            field=models.DateTimeField(blank=True, db_index=True, null=True, verbose_name='Start time'),
        ),
    ]