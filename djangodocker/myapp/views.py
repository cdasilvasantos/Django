from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import TodoList
from .forms import TodoListForm

class TodoListView(ListView):
    model = TodoList
    template_name = 'myapp/todo.html'
    context_object_name = 'todos'

class TodoCreateView(CreateView):
    model = TodoList
    form_class = TodoListForm
    template_name = 'myapp/create-todo.html'
    success_url = reverse_lazy('todo_list')

class TodoUpdateView(UpdateView):
    model = TodoList
    form_class = TodoListForm
    template_name = 'myapp/create-todo.html'
    success_url = reverse_lazy('todo_list')

class TodoDeleteView(DeleteView):
    model = TodoList
    success_url = reverse_lazy('todo_list')

def index(request):
    return render(request, 'myapp/todo.html')

def todo_view(request):
    todos = TodoList.objects.all()
    return render(request, 'myapp/todo.html', {'todos': todos})

def add_todo_view(request):
    if request.method == 'POST':
        form = TodoListForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('todo_view')  # Redirect to the todo list view after adding
    else:
        form = TodoListForm()

    return render(request, 'myapp/create-todo.html', {'form': form})
