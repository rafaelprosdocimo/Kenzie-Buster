from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models


class User(AbstractUser):
    email = models.EmailField(unique=True, max_length=127)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    birthdate = models.DateField(null=True, blank=True)
    is_employee = models.BooleanField(default=False)

    def __str__(self):
        return self.username
