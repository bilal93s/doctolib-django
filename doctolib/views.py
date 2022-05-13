from multiprocessing import context
from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render

def base(request):
    context = {"message": "Bienvenue"}
    return render(request, 'doctolib/base.html', context)