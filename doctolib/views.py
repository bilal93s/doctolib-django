from multiprocessing import context
from django.http import HttpResponse, HttpResponseRedirect
from django.views import generic
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from .models import Prestation, Profession, Appointment, prestation_practicien
from django.contrib.auth.models import User

def home_patient(request):
    current_user = request.user
    user = get_object_or_404(User, pk=current_user.id)

    return render(request, 'doctolib/home_patient.html', {
        'user': user,
    })

def base(request):
    context = {"message": "Bienvenue"}
    return render(request, 'doctolib/base.html', context)