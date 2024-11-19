from django.urls import path
from .views import (
    Home,
    TasksPage,
    Form,
    Create,
    GetTask,
)

urlpatterns = [
    path('', Home, name='home'),
    path('Tasks/', TasksPage, name='tasks'),
    path('Create/', Create, name='create'),
    path('Form/', Form, name='form'),
    path('GetTask/<int:id>/', GetTask, name='task'),
]