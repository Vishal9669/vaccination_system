from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models

class User(AbstractUser):
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=15, unique=True)

    groups = models.ManyToManyField(
        Group,
        related_name='custom_user_set',  # Prevents clash with default 'user_set'
        blank=True
    )
    user_permissions = models.ManyToManyField(
        Permission,
        related_name='custom_user_permissions_set',  # Prevents clash with default 'user_permissions_set'
        blank=True
    )
