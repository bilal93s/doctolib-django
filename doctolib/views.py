from multiprocessing import context
from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render

def base(request):
    context = {"message": "Bienvenue"}
    return render(request, 'doctolib/base.html', context)

def registration_patient(request):
    return render(request, 'doctolib/registration_patient.html')

def registration_practicien(request):
    return render(request, 'doctolib/registration_practicien.html')
