from django.urls import path
from .views import todo_view, add_todo_view



urlpatterns = [
    path('', todo_view, name='todo_view'),
     path('add/', add_todo_view, name='todo_add'),   
    path('todo/<int:pk>/', todo_view, name='todo_view'),
]

