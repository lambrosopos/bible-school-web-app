from django.shortcuts import render
from django.views.generic import CreateView
from .models import Student

def main_page(request):
    return render(request, 'pages/index.html')

class StudentCreateView(CreateView):
    model = Student
    fields = ('name', 'title', 'contact', 'memo')

def lookup_page(request):
    return render(request, 'pages/lookup.html')
