from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Play(models.Model):
    author = models.CharField(max_length=30)
    character = models.CharField(max_length=30)
    video = models.CharField(max_length=100)

class Stats(models.Model):
    author = models.CharField(max_length=30)
    character = models.CharField(max_length=30)
    image = models.FileField()

