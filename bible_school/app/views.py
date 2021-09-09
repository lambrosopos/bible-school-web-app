from django.shortcuts import render

# Create your views here.

def main_page(request):
    return render(request, 'pages/index.html')

def registration_page(request):
    return render(request, 'pages/registration.html')

def lookup_page(request):
    return render(request, 'pages/lookup.html')
