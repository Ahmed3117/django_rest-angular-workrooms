from django.db import models

from room.models import Room

# Create your models here.
class Todo(models.Model):
    room = models.ForeignKey(Room, on_delete=models.CASCADE, related_name='todos')
    title = models.CharField(max_length=255)
    is_done = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
