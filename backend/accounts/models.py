from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.
class User(AbstractUser):
    email = models.EmailField(max_length=255, null=True,unique=True)
    name = models.CharField(max_length=150)
    image = models.ImageField(upload_to='profile_images', blank=True, null=True, default='default_image.png')
    REQUIRED_FIELDS = ['name']