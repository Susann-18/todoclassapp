from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import  CreateView,ListView,DeleteView,UpdateView
from .models import Task
from .forms import TaskForm


class TaskCreateView(CreateView):
    model = Task
    form_class = TaskForm
    template_name = 'taskform.html'
    success_url = reverse_lazy('tasklist')

class TaskListView(ListView):
    model = Task
    template_name = 'tasklist.html'
    context_object_name = 'tasks'
 ##DELETE VIEWS
class TaskDeleteView(DeleteView):
    model = Task
    template_name = 'delete.html'
    success_url = reverse_lazy('tasklist')

#######UPADTE#####

class TaskUpdateView(UpdateView):
    model = Task
    form_class = TaskForm
    template_name = 'update.html'
    success_url = reverse_lazy('tasklist')





# Create your views here.
