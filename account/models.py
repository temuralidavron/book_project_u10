from calendar import month

from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.
class CustomUser(AbstractUser):
    ROLE_CHOICES = (
        ('admin', 'Admin'),
        ('reader', 'Reader'),
        ('moderator', 'Moderator')
    )
    role = models.CharField(max_length=10, choices=ROLE_CHOICES,default='moderator')
    phone=models.CharField(max_length=15)

