# Generated by Django 4.1.3 on 2022-12-05 14:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('taskplanner', '0005_remove_task_deadline'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='completed_date',
            field=models.DateField(blank=True, null=True),
        ),
    ]