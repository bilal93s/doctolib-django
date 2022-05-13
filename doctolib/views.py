from multiprocessing import context
from django.http import HttpResponse, HttpResponseRedirect
from django.views import generic
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from .models import Prestation, Profession, Appointment, prestation_practicien
from django.contrib.auth.models import User
from .forms import PriceForm

def home_patient(request):
    current_user = request.user
    user = get_object_or_404(User, pk=current_user.id)

    return render(request, 'doctolib/home_patient.html', {
        'user': user,
    })

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

def base(request):
    context = {"message": "Bienvenue"}
    return render(request, 'doctolib/base.html', context)