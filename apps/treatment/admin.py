from django.contrib import admin

from apps.treatment.models import TreatmentPatient, Treatment

admin.site.register(TreatmentPatient)
admin.site.register(Treatment)
