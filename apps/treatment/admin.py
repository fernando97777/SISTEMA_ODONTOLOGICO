from django.contrib import admin

from apps.treatment.models import TreatmentPatient, Treatment, QuotesPatient,Prescription

admin.site.register(TreatmentPatient)
admin.site.register(Treatment)
admin.site.register(QuotesPatient)
admin.site.register(Prescription)
