from django.forms import ModelForm
from django import forms
from .models import Task


class DateInput(forms.DateInput):
    input_type = "date"

class TaskForm(ModelForm):
    class Meta:
        widgets = {"limit_date" : DateInput()}
        model = Task
        fields = ["title", "task_description", "limit_date", "box_choices"]