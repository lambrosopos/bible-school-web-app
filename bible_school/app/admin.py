from django.contrib import admin

from .models import Student, Church

class StudentAdmin(admin.ModelAdmin):
    list_display = ("name", "title", "contact", "memo")

class ChurchAdmin(admin.ModelAdmin):
    list_display = ("name", "contact")

admin.site.register(Church, ChurchAdmin)
admin.site.register(Student, StudentAdmin)
