from django.db import models
from django.contrib.auth.models import AbstractUser



class User(AbstractUser):
    name = models.CharField(max_length=50)
    phone = models.CharField(max_length=13)
    password = models.CharField(max_length=16)

    def __str__(self):
        return f"{self.name} {self.username}"
 