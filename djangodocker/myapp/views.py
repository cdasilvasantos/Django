from django.shortcuts import render
from django.urls import reverse_lazy
from .views import  StudentCreateView, StudentUpdateView, StudentDeleteView
from .models import Student
# Create your views here.

def index(request):
    return render(request, 'myapp/index.html')


class TodoListView(ListView):
    model = todoList
    template_name = 'myapp/todo_list.html'
    context_object_name = 'todos'

class TodoCreateView(CreateView):
    model = todoList
    template_name = 'myapp/todo_form.html'
    fields = ['this_item', 'time']
    success_url = reverse_lazy('todo_list')

class TodoUpdateView(UpdateView):
    model = todoList
    template_name = 'myapp/todo_form.html'
    fields = ['this_item', 'time']
    success_url = reverse_lazy('todo_list')

class TodoDeleteView(DeleteView):
    model = todoList
    template_name = 'myapp/todo_confirm_delete.html'
    success_url = reverse_lazy('todo_list')




