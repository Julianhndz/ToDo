from django.forms import ModelForm
from django import forms
from .models import Task

# Clase para generar el widged de seleccion de fecha en el "front"
class DateInput(forms.DateInput):
    input_type = "date"

class TaskForm(ModelForm):
    class Meta:
        widgets = {"limit_date" : DateInput()} # Linea que agrega el widget desde la clase ya creada.
        model = Task
        fields = ["title", "task_description", "limit_date", "box_choices"]