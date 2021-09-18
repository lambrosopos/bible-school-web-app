from django.db import models
from django.core.validators import RegexValidator
from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.
class Church(models.Model):
    name = models.CharField(max_length=128)
    contact = PhoneNumberField(unique=True, null=True, blank=True, region='KR')

    class Meta:
        verbose_name_plural = "churches"

    def __str__(self):
        return self.name

class Title(models.Model):
    name = models.CharField(max_length=16)
    
    class Meta:
        verbose_name_plural = "titles"

    def __str__(self):
        return self.name

class Cohort(models.Model):
    name = models.CharField(max_length=128)
    memo = models.CharField(max_length=255)

    class Meta:
        verbose_name_plural = "cohorts"

    def __str__(self):
        return self.name

class Student(models.Model):
    name = models.CharField(max_length=64)
    contact = PhoneNumberField(unique=True, null=False, blank=False, region='KR')
    memo = models.TextField(blank=True)

    cohort = models.ForeignKey(
        Cohort,
        on_delete=models.CASCADE
    )
    title = models.ForeignKey(
        Title,
        on_delete=models.CASCADE
    )
    church = models.ForeignKey(
        Church,
        on_delete=models.CASCADE
    )

    class Meta:
        verbose_name_plural = "students"

    def __str__(self):
        return self.name
