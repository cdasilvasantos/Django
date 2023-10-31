from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'myapp/index.html')

class StudentListView(ListView):
    model = Student

class StudentCreateView(CreateView):
    model = Student
    fields = ['first_name', 'last_name', 'email']
