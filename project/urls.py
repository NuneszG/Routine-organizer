from django.urls import path
from .views import (
    Home,
    TasksPage,
)

urlpatterns = [
    path('', Home, name='home'),
    path('Tasks/', TasksPage, name='tasks'),
]