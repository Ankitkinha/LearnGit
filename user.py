from django.db import models
from django.contrib.auth.models import AbstractUser


class User(models.Model):
    name = models.CharField(max_length=50)
    profile_pic_url = models.CharField(max_length=300)
    password = models.CharField(max_length=200)

    def __str__(self):
        return self.name
