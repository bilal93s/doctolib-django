from multiprocessing import context
from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render,  redirect
from . forms import NewPatientForm, NewPracticientForm
from django.contrib.auth import login
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
            return redirect("main:homepage")
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
            return redirect("main:homepage")
        messages.error(request, "Unsuccessful registration. Invalid information.")
    form = NewPracticientForm()
    return render (request=request, template_name="doctolib/registration_practicien.html", context={"register_form":form})
    return render(request, 'doctolib/registration_practicien.html')


def reservation(request):
    # if request.method == "POST":
    #     form = NewUserForm(request.POST)
    #     if form.is_valid():
    #         user = form.save()
    #         login(request, user)
    #         messages.success(request, "Registration successful." )
    #         return redirect("main:homepage")
    #     messages.error(request, "Unsuccessful registration. Invalid information.")
    # form = NewUserForm()
    return render (request=request, template_name="main/register.html", context={"register_form":form})
from django.http import HttpResponse, HttpResponseRedirect
from django.views import generic
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from .models import Prestation, Profession, Appointment, prestation_practicien
from django.contrib.auth.models import User

