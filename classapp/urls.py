from django.urls import path

from .views import TaskCreateView,TaskListView,TaskDeleteView,TaskUpdateView

urlpatterns=[
    path('new/', TaskCreateView.as_view(), name='task_create'),
    path('', TaskListView.as_view(), name='tasklist'),
    path('task/<int:pk>/delete/', TaskDeleteView.as_view(), name='task_delete'),
    path('tasks/<int:pk>/update/', TaskUpdateView.as_view(), name='task_update'),
    
]