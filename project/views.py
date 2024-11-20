from django.shortcuts import render, redirect
from .models import Task

def Home(request):
    return render(request, 'home.html')


def TasksPage(request):
    task = Task.objects.all()
    
    return render(request, 'tasks.html', {'tasks': task})

def Form(request):
    return render(request, 'form.html')

def Create(request):
    title = request.POST.get('title')
    caption = request.POST.get('caption')
    content = request.POST.get('content')

    task = Task.objects.create(
        title = title,
        caption = caption,
        content = content
    )

    return redirect('tasks')

def GetTask(request, id):
    task = Task.objects.get(id=id)

    return render(request, 'task.html', {'task': task})


def EditTask(request, id):
    task = Task.objects.get(id=id)

    return render(request, 'update.html', {'task': task})


def UpdateTask(request, id):
    task = Task.objects.get(id=id)

    title = request.POST.get('title')
    caption = request.POST.get('caption')
    content = request.POST.get('content')

    task.title = title
    task.caption = caption
    task.content = content
    task.save()

    return redirect('tasks')


def DeleteTask(request, id):
    
    try:
        task = Task.objects.get(id=id)
        task.delete()

    except:
        print('Task not found, try again.')
        return False

    return redirect('tasks')