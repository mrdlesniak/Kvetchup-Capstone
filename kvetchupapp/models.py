from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class Site(models.Model):
    name = models.CharField(max_length=200)
    url = models.URLField(max_length=200)
    email = models.EmailField(max_length=254)
    phone_number = models.CharField(max_length=200, default="xxx-xxx-xxxx")
    #each site can have many complaints from many users. 
    #users can have many complaints to many sites.
    #complaints can have only one user and only one site. 

    def __str__(self):
        return f"Name: {self.name} | Id: {self.id}"

class Complaint(models.Model):
    complaint = models.TextField()
    user = models.ForeignKey(User, on_delete=models.PROTECT, null=True, blank=True, related_name="complaints")
    site = models.ForeignKey(Site, on_delete=models.PROTECT, null=True, blank=True, related_name="complaints") 

    def __str__(self):
        return self.complaint