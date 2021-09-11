from django.forms import modelformset_factory
from django.shortcuts import render
from django.views.generic import UpdateView
from .models import Student
from .forms import StudentForm

def main_page(request):
    return render(request, 'pages/index.html')

def registration_page(request):
    StudentFormSet = modelformset_factory(Student,
                                          fields=(
                                              'name',
                                              'title',
                                              'contact',
                                              'memo')
                                         )
    if request.method == 'POST':
        formset = StudentFormSet(request.POST, request.FILES)
        if formset.is_valid():
            formset.save()
    else:
        formset = StudentFormSet()

    return render(request,
                  'pages/registration.html',
                  {'formset':formset})

# class StudentCreateView(UpdateView):
    # model = Student
    # form_class = StudentForm
    # template_name = 'pages/registration_page.html'

def lookup_page(request):
    return render(request, 'pages/lookup.html')
