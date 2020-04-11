from django.db import models
from django.contrib.postgres.fields import JSONField, ArrayField


# Create your models here.
class User(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, unique=True)
    email = models.CharField(max_length=100, unique=True)
    password = models.CharField(max_length=100, unique=True)

    class Meta:
        ordering = ['id']
