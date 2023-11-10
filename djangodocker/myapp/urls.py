# urls.py
from django.urls import path
from .views import record_list, record_detail, record_edit, record_delete, record_create

urlpatterns = [
    path('records/', record_list, name='record_list'),
    path('records/<int:pk>/', record_detail, name='record_detail'),
    path('records/<int:pk>/edit/', record_edit, name='record_edit'),
    path('records/<int:pk>/delete/', record_delete, name='record_delete'),
    path('records/create/', record_create, name='record_create'),
    # Add other URLs for create, update, delete views
]
