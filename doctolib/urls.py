from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.base, name='base'),
    path('registration_patient', views.registration_patient, name='registration_patient'),
    path('registration_practicien', views.registration_practicien, name='registration_practicien'),
]
