from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Task(models.Model):
    title = models.CharField(max_length=60)
    task_description = models.TextField()
    creation_date = models.DateTimeField(auto_now_add=True)
    limit_date = models.DateTimeField(null=True)
    finished_date = models.DateTimeField(blank=True, null=True, auto_now=True)
    list_choices = [("Pendiente", "Pendiente"),
               ("En progreso", "En progreso"),
               ("Completada", "Completada")]
    box_choices = models.CharField(max_length=30, blank=True, null=True, choices=list_choices)
    id_user = models.ForeignKey(User, on_delete=models.CASCADE)


    def __str__(self):
        return self.title
