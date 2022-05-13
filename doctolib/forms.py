from django import forms
from .models import Appointment, Profession

class PriceForm(forms.Form):
    your_price = forms.IntegerField(required=True)

    def save(self, commit=True):
            appointment = super(PriceForm, self).save(commit=False)
            appointment.price_prestation = self.cleaned_data['your_price']
            if commit:
                appointment.save()
            return appointment