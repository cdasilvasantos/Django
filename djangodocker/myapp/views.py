from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import todoList
# Create your views here.

def index(request):
    return render(request, 'myapp/todo.html')


class TodoListView(ListView):
    model = todoList
    template_name = 'myapp/todo.html'
    context_object_name = 'todos'

class TodoCreateView(CreateView):
    model = todoList
    template_name = 'myapp/create-todo.html'
    fields = ['this_item', 'time']
    success_url = reverse_lazy('todos')

class TodoUpdateView(UpdateView):
    model = todoList
    template_name = 'myapp/todo.html'
    fields = ['this_item', 'time']
    success_url = reverse_lazy('todo_list')

class TodoDeleteView(DeleteView):
    model = todoList
    template_name = 'myapp/todo.html'
    success_url = reverse_lazy('todo_list')




