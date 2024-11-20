from django.urls import path
from .views import (
    Home,
    Form,
    Create,
    GetTask,
    TasksPage,
    EditTask,
    UpdateTask,
    DeleteTask,
    
)

urlpatterns = [
    path('', Home, name='home'),
    path('Tasks/', TasksPage, name='tasks'),
    path('Create/', Create, name='create'),
    path('Form/', Form, name='form'),
    path('GetTask/<int:id>/', GetTask, name='task'),
    path('UpdateTask/<int:id>/', UpdateTask, name='update'),
    path('EditTask/<int:id>/', EditTask, name='edit'),
    path('DeleteTask/<int:id>/', DeleteTask, name='delete'),
    
]