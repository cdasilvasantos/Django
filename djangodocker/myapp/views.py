from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import Student

# Create your views here.

def index(request):
    return render(request, 'myapp/index.html')

class StudentListView(ListView):
    model = Student

class StudentCreateView(CreateView):
    model = Student
    fields = ['first_name', 'last_name', 'email']

class StudentUpdateView(UpdateView):
    model = Student
    fields = ['first_name', 'last_name', 'email']

class StudentDeleteView(DeleteView):
    model = Student
    success_url = reverse_lazy('student_list')
