from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class CustomUser(AbstractUser):
    ROLES = (
        ('cliente', 'Cliente'),
        ('admin', 'Administrador'),
    )
    role = models.CharField(max_length = 10, choices=ROLES, default='cliente')

    def __str__(self):
        return f"{self.username} ({self.role})"