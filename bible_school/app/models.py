from django.db import models
from django.core.validators import RegexValidator
from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.
class Church(models.Model):
    name = models.CharField(max_length=128)
    contact = PhoneNumberField(unique=True, region='KR')

    class Meta:
        verbose_name_plural = "churches"

    def __str__(self):
        return self.name

class Student(models.Model):
    name = models.CharField(max_length=64)
    title = models.CharField(max_length=128, blank=True)
    contact = PhoneNumberField(unique=True, null=False, blank=False, region='KR')
    memo = models.TextField(blank=True)
    church = models.ForeignKey(
        Church,
        on_delete=models.CASCADE
    )

    class Meta:
        verbose_name_plural = "students"

    def __str__(self):
        return self.name
