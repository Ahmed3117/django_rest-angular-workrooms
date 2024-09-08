import random
from django.db import models
import string
from accounts.models import User
# Create your models here.

def generate_random_id():
    letters = string.ascii_letters
    numbers = string.digits 
    digits = 8
    return ''.join(random.choices(letters + numbers, k=digits))
    

class Room(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    room_id = models.CharField(max_length=8, unique=True, default=generate_random_id)
    created_at = models.DateTimeField(auto_now_add=True)
    is_done = models.BooleanField(default=False)
    members = models.ManyToManyField(User)
    admin = models.ForeignKey(User, related_name='room_admin', on_delete=models.SET_NULL, blank=True, null=True)
    
    def __str__(self):
        return self.title
    
