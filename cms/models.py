from django.db import models

# Create your models here.
class Site(models.Model):
    id = models.AutoField(primary_key=True)
    code = models.CharField(max_length=100, unique=True)
    name = models.CharField(max_length=100)

    class Meta:
        ordering = ['id']


class Plant(models.Model):
    id = models.AutoField(primary_key=True)
    code = models.CharField(max_length=100, unique=True)
    name = models.CharField(max_length=100)
    site = models.ForeignKey(Site, on_delete=models.PROTECT)
    admins = models.ManyToManyField(User, related_name='plant')

    class Meta:
        ordering = ['id']

