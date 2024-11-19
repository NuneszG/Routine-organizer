from django.shortcuts import render
from .models import Task

def Home(request):
    return render(request, 'home.html')


def TasksPage(request):
    task = Task.objects.all()
    
    return render(request, 'tasks.html', {'task': task})

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

    return render(request, 'tasks.html', {'task': task})

def GetTask(request, id):
    task = Task.objects.get(id=id)

    return render(request, 'task.html', {'task': task})
