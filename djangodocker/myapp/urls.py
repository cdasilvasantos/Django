from django.urls import path
from .views import TodoListView, TodoCreateView, TodoUpdateView, TodoDeleteView, index, todo_view, add_todo_view

urlpatterns = [
    path('', index, name='index'),
    path('todos/', TodoListView.as_view(), name='todo_list'),
    path('todo/<int:pk>/', TodoUpdateView.as_view(), name='todo_update'),
    path('todo/create/', TodoCreateView.as_view(), name='todo_create'),
    path('todo/<int:pk>/delete/', TodoDeleteView.as_view(), name='todo_delete'),
    path('todo/', todo_view, name='todo_view'),
    path('add_todo/', add_todo_view, name='add_todo_view'),
]
