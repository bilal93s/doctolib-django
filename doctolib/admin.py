from django.contrib import admin

from .models import Prestation
from .models import Profession
from .models import Appointment
from .models import prestation_practicien

admin.site.register(Prestation)
admin.site.register(Profession)
admin.site.register(Appointment)
admin.site.register(prestation_practicien)