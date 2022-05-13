from django.db import models
from django.forms import ModelForm
from django.contrib.auth.models import User


class Prestation(models.Model):
    titre = models.CharField(max_length=200)
    price = models.IntegerField()

    def __str__(self):
        return self.titre
    
class Profession(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    description = models.CharField(max_length=200)
    prestations = models.ForeignKey(Prestation, on_delete=models.CASCADE)

    def __str__(self):
        return self.description

class Appointment(models.Model):
    date = models.DateTimeField('appointment date')
    practicien = models.ForeignKey(User, on_delete=models.CASCADE)
    patient = models.ForeignKey(User, related_name='%(class)s_patient_created', on_delete=models.CASCADE)
    prestation = models.ForeignKey(Prestation, on_delete=models.CASCADE)  

class prestation_practicien(models.Model):
    profession = models.ForeignKey(Profession, on_delete=models.CASCADE)
    practicien = models.ForeignKey(User, on_delete=models.CASCADE)
    price = models.IntegerField()

class AppointmentForm(ModelForm):
    class Meta:
        model = Appointment
        fields = ['date', 'practicien', 'prestation']