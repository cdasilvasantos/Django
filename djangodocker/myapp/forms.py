# forms.py
from django import forms
from .models import TodoList

class TodoListForm(forms.ModelForm):
    class Meta:
        model = TodoList
        fields = ['this_item', 'time']  # List all fields you want to include in your form
