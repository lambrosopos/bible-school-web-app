from django.db.models import Q
from django.shortcuts import render, redirect
from .forms import StudentForm
from .models import Student

def main_page(request):
    return render(request, 'pages/index.html')


def lookup_page(request):
    context = {}
    if request.method == "POST":
        query_q = request.POST.get('q', '')

        query_results = Student.objects.filter(
            Q(name__icontains=query_q)
        )

        context["results"] = [_ for _ in query_results.values_list()]

    return render(request, 'pages/lookup.html', {'context':context})


def student_registration(request):
    if request.method == "POST":
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('main_page')
    else:
        form = StudentForm()
    return render(request, 'student/student_form.html', {'form':form})

def student_lookup(request):
    pass
