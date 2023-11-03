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
    template_name = 'myapp/student_list.html'  # Specify your template name here
    success_url = reverse_lazy('student_list')

class StudentUpdateView(UpdateView):
    model = Student
    fields = ['first_name', 'last_name', 'email']
    template_name = 'myapp/student_list.html'  # Specify your template name here
    success_url = reverse_lazy('student_list')

class StudentDeleteView(DeleteView):
    model = Student
    template_name = 'myapp/student_list.html'  # Specify your template name here
    success_url = reverse_lazy('student_list')  # Use the name of your list view url