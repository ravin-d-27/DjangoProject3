# Generated by Django 4.1.3 on 2022-12-06 08:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('taskplanner', '0008_task_completed'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='time_req',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
