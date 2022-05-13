from multiprocessing import context
from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render,  redirect, get_object_or_404
from . forms import NewPatientForm, NewPracticientForm
from .models import Prestation, Profession, Appointment, prestation_practicien
from django.contrib.auth import login
from django.contrib.auth.models import User
from .forms import PriceForm
from django.contrib import messages

def base(request):
    context = {"message": "Bienvenue"}
    return render(request, 'doctolib/base.html', context)

def home_patient(request):
    current_user = request.user
    user = get_object_or_404(User, pk=current_user.id)

    return render(request, 'doctolib/home_patient.html', {
        'user': user,
    })

def registration_patient(request):
    if request.method == "POST":
        form = NewPatientForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Registration successful." )
            return redirect("doctolib:home_patient")
        messages.error(request, "Unsuccessful registration. Invalid information.")
    form = NewPatientForm()
    return render (request=request, template_name="doctolib/registration_patient.html", context={"register_form":form})

def registration_practicien(request):
    if request.method == "POST":
        form = NewPracticientForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Registration successful." )
            return redirect("doctolib:home_patient")
        messages.error(request, "Unsuccessful registration. Invalid information.")
    form = NewPracticientForm()
    return render (request=request, template_name="doctolib/registration_practicien.html", context={"register_form":form})
    return render(request, 'doctolib/registration_practicien.html')

def backoffice_practicien(request):
    current_user = request.user
    user = get_object_or_404(User, pk=current_user.id)

    return render(request, 'doctolib/backoffice_practicien.html', {
        'user': user,
    })

def invoice(request, appointment_id):
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = PriceForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            appointment = form.save()
            Appointment(request, appointment)
            messages.success(request, "Prix modifié avec succès." )
            return redirect("main:homepage")
        messages.error(request, "Echec de modif prix")
    form = PriceForm()
    return render (request=request, template_name="doctolib/invoice.html", context={"form":form})
    return render(request, 'doctolib/invoice.html.html')
