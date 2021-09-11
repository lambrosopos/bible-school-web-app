from django.db import models

# Create your models here.

class Student(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=64, blank=True)
    title = models.CharField(max_length=128, blank=True)
    contact = models.IntegerField()
    memo = models.TextField(blank=True)
