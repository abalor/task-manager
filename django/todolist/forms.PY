from django import forms
from .models import Task

class TaskForm(forms.ModelForm):
    due_date = forms.DateTimeField(widget=forms.TextInput(attrs={'type': 'datetime-local'}))
    reminder_time = forms.IntegerField(min_value=0, label='Remind me (in minutes)')
 
    class Meta:
        model = Task
        fields = ['title', 'description', 'due_date', 'reminder_time']