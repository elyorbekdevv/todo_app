from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
from .forms import  *

def hello(request):
    form = TaskForm()
    tasks = Task.objects.all()
    if request.method == "POST":
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/')
    context = {'tasks': tasks, 'form':form}
    return render(request, 'list.html', context)

def updatetask(request, pk):
    task = Task.objects.get(id=pk)
    form = TaskForm(instance=task)

    if request.method == 'POST':
        form = TaskForm(data=request.POST , instance=task )
        if form.is_valid:
            form.save()
        return redirect('/')
    context = {'form':form,}
    return render(request, 'update_task.html', context)

def deletetask(request, pk):
    item = Task.objects.get(id=pk)
    if request.method == 'POST':
        item.delete()
        return redirect('/')
    context = {'item':item,}
    return render(request, 'delete.html', context)
