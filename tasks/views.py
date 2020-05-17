from django.shortcuts import render, redirect
from .models import *
from .forms import *
# Create your views here.

def task_list(request):
    form = TaskForm()
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('task_list')

    taskslist = task.objects.all()
    context = {'taskslist':taskslist, 'form':form}
    return render(request, 'tasks.html', context)

def task_update(request, pk):
    instance_task = task.objects.get(id=pk)
    form = TaskForm(instance=instance_task)
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=instance_task)
        if form.is_valid():
            form.save()
            return redirect('task_list')
    context = {'form':form}
    return render(request, 'task_update.html', context)

def task_delete(request, pk):
    instance_task = task.objects.get(id=pk)
    if request.method == 'POST':
        instance_task.delete()
        return redirect('task_list')
    context = {'task':instance_task}
    return render(request, 'task_delete.html', context)
