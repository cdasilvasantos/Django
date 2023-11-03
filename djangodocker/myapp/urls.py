from django.urls import path, include
from .views import StudentListView, StudentCreateView, StudentUpdateView, StudentDeleteView

urlpatterns = [

    # path('admin/', admin.site.urls),
    path('', StudentListView.as_view(), name='student_list'),
    path('new/', StudentCreateView.as_view(), name='student_new'),
    path('new/', StudentCreateView.as_view(), name='student_create'),  # Ensure this is named 'student_create'
    path('<int:pk>/edit/', StudentUpdateView.as_view(), name='student_update'),  # Ensure this is named 'student_update'
    path('<int:pk>/edit/', StudentUpdateView.as_view(), name='student_edit'),
    path('<int:pk>/delete/', StudentDeleteView.as_view(), name='student_delete'),
]
