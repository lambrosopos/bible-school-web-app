from django.db.models import Q
from django.shortcuts import render, redirect
from .forms import StudentForm
from .models import Student, Church

def main_page(request):
    return render(request, 'pages/index.html')


def lookup_page(request):
    context = {}

    church_list = Church.objects.all()

    context["churches"] = [{"id":_['id'], "name":_['name']} for _ in church_list.values()]

    if request.method == "POST":
        query_q = request.POST.get('q', '')

        query_results = Student.objects.filter(
            Q(name__icontains=query_q)
        )

        context["results"] = list(range(len(query_results)))

        for idx, record in enumerate(query_results):
            context["results"][idx] = (
                (
                    record.name,
                    record.group,
                    record.cohort.name
                )
            )

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
