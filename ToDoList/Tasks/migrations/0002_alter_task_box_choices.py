# Generated by Django 4.2.4 on 2023-09-13 20:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Tasks', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='box_choices',
            field=models.CharField(blank=True, choices=[('Pendiente', 'Pendiente'), ('En progreso', 'En progreso'), ('Completada', 'Completada')], max_length=30, null=True),
        ),
    ]
