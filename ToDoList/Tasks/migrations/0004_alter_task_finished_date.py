# Generated by Django 4.2.4 on 2023-09-19 21:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Tasks', '0003_task_finished_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='finished_date',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
    ]
