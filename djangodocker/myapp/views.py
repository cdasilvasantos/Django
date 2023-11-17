from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import todoList
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseRedirect
from .forms import TodoListForm
# Create your views here.

def index(request):
    return render(request, 'myapp/todo.html')


def todo_view(request, pk=None):
    todo = None
    if pk:
        todo = get_object_or_404(todoList, pk=pk)
        form = TodoListForm(request.POST or None, instance=todo)
    else:
        form = TodoListForm(request.POST or None)

    if request.method == 'POST' and form.is_valid():
        form.save()
        return redirect('todo_view')

    if request.method == 'GET' and 'delete' in request.GET:
        pk_to_delete = request.GET.get('delete')
        todoList.objects.filter(pk=pk_to_delete).delete()
        return redirect('todo_view')

    todos = todoList.objects.all()

    # Use 'todo_form.html' for GET request when adding/editing a todo
    # if request.method == 'GET' and (pk or not todos):
    #     return render(request, 'myapp/create-todo.html', {'form': form})

    # Use 'todo.html' to display the list of todos
    return render(request, 'myapp/todo.html', {'todos': todos, 'form': form})


def add_todo_view(request):
    if request.method == 'POST':
        form = TodoListForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('todo_view')  # Redirect to the todo list view after adding
    else:
        form = TodoListForm()

    return render(request, 'myapp/create-todo.html', {'form': form})




