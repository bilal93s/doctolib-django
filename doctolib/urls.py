from django.contrib import admin
from django.urls import path
from . import views

app_name = 'doctolib'
urlpatterns = [
    path('home_patient/', views.home_patient, name='home_patient'),
    path('backoffice_practicien/', views.backoffice_practicien, name='backoffice_practicien'),
    path('<int:appointment_id>/invoice/', views.invoice, name='invoice'),
    path('', views.base, name='base'),
]
