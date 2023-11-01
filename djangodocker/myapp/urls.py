from django.urls import path, include
from .views import StudentListView, StudentCreateView, StudentUpdateView, StudentDeleteView

urlpatterns = [

    # path('admin/', admin.site.urls),
    path('', StudentListView.as_view(), name='student_list'),
    path('new/', StudentCreateView.as_view(), name='student_new'),
    path('<int:pk>/edit/', StudentUpdateView.as_view(), name='student_edit'),
    path('<int:pk>/delete/', StudentDeleteView.as_view(), name='student_delete'),
]
