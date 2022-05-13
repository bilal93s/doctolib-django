from django.contrib import admin
from django.urls import path
from . import views

app_name = 'doctolib'
urlpatterns = [
    path('home_patient/', views.home_patient, name='home_patient'),
    path('', views.base, name='base'),
    path('registration_patient', views.registration_patient, name='registration_patient'),
    path('registration_practicien', views.registration_practicien, name='registration_practicien'),
]
