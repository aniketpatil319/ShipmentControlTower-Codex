from django.contrib.auth.models import AbstractUser
from django.db import models


class Company(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self) -> str:
        return self.name


class User(AbstractUser):
    company = models.ForeignKey(Company, on_delete=models.CASCADE, related_name='users')

    def __str__(self) -> str:
        return f"{self.username} ({self.company})"
