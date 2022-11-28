from django.db import models

# Create your models here.
from django.db import models
from django.utils import timezone


class Books(models.Model):
    title = models.CharField(max_length=100)
    price = models.FloatField(default=0)
    stock = models.IntegerField(default=0)
    image = models.CharField(max_length=2083, blank=True, null=True)
    author = models.CharField(max_length=100)

    def __str__(self):
        return self.title