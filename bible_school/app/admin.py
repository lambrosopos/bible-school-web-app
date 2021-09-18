from django.contrib import admin

from .models import Student, Church, Title

class StudentAdmin(admin.ModelAdmin):
    list_display = ("name", "title", "contact", "memo")

class ChurchAdmin(admin.ModelAdmin):
    list_display = ("name", "contact")

class TitleAdmin(admin.ModelAdmin):
    list_diplay = ("name")

admin.site.register(Title, TitleAdmin)
admin.site.register(Church, ChurchAdmin)
admin.site.register(Student, StudentAdmin)
