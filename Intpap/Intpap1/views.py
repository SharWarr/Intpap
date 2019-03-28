from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return render(request , 'Intpap1/home.html')

# Create your views here.

def sem1(request):
    return render(request, 'Intpap1/semester1.html')
