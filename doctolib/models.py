from django.db import models
from django.contrib.auth.models import User


class Prestation(models.Model):
    titre = models.CharField(max_length=200)
    price = models.IntegerField(default=0)

    def __str__(self):
        return self.titre
    
class Profession(models.Model):
    user = models.ForeignKey(User, related_name='practicien_profession', on_delete=models.CASCADE)
    description = models.CharField(max_length=200)
    prestations = models.ForeignKey(Prestation, on_delete=models.CASCADE)

    def __str__(self):
        return self.description

class Appointment(models.Model):
    date = models.DateTimeField('appointment date')
    practicien = models.ForeignKey(User, related_name='practicien_appointments', on_delete=models.CASCADE)
    patient = models.ForeignKey(User, related_name='patient_appointments', on_delete=models.CASCADE)
    prestation = models.ForeignKey(Prestation, on_delete=models.CASCADE)
    price_prestation = models.IntegerField(default=0)

class prestation_practicien(models.Model):
    profession = models.ForeignKey(Profession, on_delete=models.CASCADE)
    practicien = models.ForeignKey(User, on_delete=models.CASCADE)
    price = models.IntegerField()
