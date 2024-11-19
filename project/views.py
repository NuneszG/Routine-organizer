from django.shortcuts import render
from .models import Task

def Home(request):
    return render(request, 'home.html')
