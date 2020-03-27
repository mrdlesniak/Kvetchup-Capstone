from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    phone = models.CharField(max_length=20)
    location = models.CharField(max_length=100)
    image = models.ImageField(upload_to='profile_images/', null=True, blank=True)


    def __str__(self):
        return self.username
