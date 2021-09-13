from django.db import models
from django.core.validators import RegexValidator
from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.

class Student(models.Model):

    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=64)
    title = models.CharField(max_length=128, blank=True)
    
    contact = PhoneNumberField(unique=True, null=False, blank=False, region='KR')

    memo = models.TextField(blank=True)
