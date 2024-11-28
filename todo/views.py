# Create your views here.
## a method to list our tasks
## a method to create the tasks
# method to list task
from django.shortcuts import render, redirect, get_object_or_404
from .models import Task
from .forms import TaskForm


def task_list(request):
    # all records in the db
    # rows : represent the object /columns
    tasks = Task.objects.all()
    # return jSON format
    '''
      id, title , completed 
      [
      {
        "id" : 1,
        "title" : "Task 1",
        "completed" : False
      },
      {
        "id" : 2,
        "title" : "Task 1",
        "completed" : False
      }
      --------

      ]
    '''
    return render(request, 'todo/task_list.html', {'tasks': tasks})


def task_create(request):
    # cover validity
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('task_list')
    else:
        form = TaskForm()
    return render(request, 'todo/task_form.html', {'form': form})


def task_delete(request, pk):
    task = get_object_or_404(Task, pk=pk)
    if request.method == 'POST':
        task.delete()
        return redirect('task_list')
    return render(request, 'todo/task_confirm_delete.html',
                  {'task': task})


def task_update(request, pk):
    task = get_object_or_404(Task, pk=pk)
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('task_list')
    else:
        form = TaskForm(instance=task)
    return render(request, 'todo/task_form.html',
                  {'form': form})