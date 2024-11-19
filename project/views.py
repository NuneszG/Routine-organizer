from django.shortcuts import render
from .models import Task

def Home(request):
    return render(request, 'home.html')


def TasksPage(request):
    task = Task.objects.all()
    
    return render(request, 'tasks.html', {'task': task})
