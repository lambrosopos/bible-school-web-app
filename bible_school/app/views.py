from django.db.models import Q
from django.shortcuts import render, redirect
from .forms import StudentForm
from .models import Student, Church, CohortStudentJoin

def main_page(request):
    return render(request, 'pages/index.html')


def lookup_page(request):
    context = {}

    church_list = Church.objects.all()

    context["churches"] = [{"id":_['id'], "name":_['name']} for _ in church_list.values()]

    if request.method == "POST":
        student_name = request.POST.get('student_name', '')
        church_id = request.POST.get('church_id', '')

        if church_id:
            query_results = Student.objects.filter(
                Q(name__icontains=student_name) & Q(church_id=church_id)
            )
        else:
            query_results = Student.objects.filter(
                Q(name__icontains=student_name)
            )

        if query_results:
            context["results"] = list(range(len(query_results)))

            for idx, record in enumerate(query_results):
                context["results"][idx] = (
                    (
                        record.id,
                        record.name,
                        record.title.name,
                        str(record.contact)[-4:],
                        record.cohort.name if record.cohort else '',
                        record.church.name
                    )
                )

    return render(request, 'pages/lookup.html', context)


def student_registration(request):
    if request.method == "POST":
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('main_page')
    else:
        form = StudentForm()
    return render(request, 'student/student_form.html', {'form':form})

def student_group(request, student_id):
    context = {}

    student = Student.objects.filter(
        Q(id=student_id)
    )[0]

    context["student_name"] = student.name
    context["title_name"] = student.title.name
    context["church_name"] = student.church.name
    context["cohort_name"] = student.cohort.name if student.cohort else ''

    query_results = CohortStudentJoin.objects.filter(
        Q(student_id=student_id)
    )

    context["results"] = list(range(len(query_results)))

    for idx, record in enumerate(query_results):
        context['results'][idx] = (
            record.group,
            '리더' if record.leader else '조원'
        )

    return render(request, 'student/student_group.html', context)
