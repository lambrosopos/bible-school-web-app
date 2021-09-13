from django.shortcuts import render, redirect
from .forms import StudentForm

def main_page(request):
    return render(request, 'pages/index.html')

def lookup_page(request):
    return render(request, 'pages/lookup.html')

def student_registration(request):
    if request.method == "POST":
        form = StudentForm(request.POST)
        if form.is_valid():
            return redirect('main_page')
    else:
        form = StudentForm()
    return render(request, 'student/student_form.html', {'form':form})
