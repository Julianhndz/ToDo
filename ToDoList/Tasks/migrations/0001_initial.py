# Generated by Django 4.2.4 on 2023-08-25 18:52

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=60)),
                ('task_description', models.TextField()),
                ('creation_date', models.DateTimeField(auto_now_add=True)),
                ('limit_date', models.DateTimeField(null=True)),
                ('box_choices', models.CharField(blank=True, choices=[('toDo', 'Pendiente'), ('InProgress', 'En progreso'), ('Completed', 'Completada')], max_length=10, null=True)),
                ('id_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]