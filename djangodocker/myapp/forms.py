# forms.py
from django import forms
from .models import todoList

class TodoListForm(forms.ModelForm):
    class Meta:
        model = todoList
        fields = ['this_item', 'time']  # List all fields you want to include in your form
