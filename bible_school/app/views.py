from django.forms import modelformset_factory
from django.shortcuts import render
from django.views.generic import CreateView, UpdateView
from .models import Student
from .forms import StudentForm

def main_page(request):
    return render(request, 'pages/index.html')

def lookup_page(request):
    return render(request, 'pages/lookup.html')

class StudentCreateView(CreateView):
    model = Student
    fields = ( 'name', 'title', 'contact', 'memo' )

class StudentUpdateView(UpdateView):
    model = Student
    fields = ( 'name', 'title', 'contact', 'memo' )
