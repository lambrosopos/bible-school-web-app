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
        student_name = request.POST.get('student_name', '')
        church_id = request.POST.get('church_id', '')

        query_results = Student.objects.filter(
            Q(name__icontains=student_name) & Q(church_id=church_id)
        )

        context["results"] = list(range(len(query_results)))

        for idx, record in enumerate(query_results):
            context["results"][idx] = (
                (
                    record.name,
                    record.title.name,
                    str(record.contact)[-4:],
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
