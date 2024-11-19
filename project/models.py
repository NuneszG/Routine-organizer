from django.db import models

class Task(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=80)
    content = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
