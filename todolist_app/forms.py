from django import forms
from todolist_app.models import TasksList

class Taskform(forms.ModelForm):
    class Meta:
        model = TasksList
        fields = ['task','done_status']