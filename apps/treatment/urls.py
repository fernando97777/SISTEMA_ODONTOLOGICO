from django.contrib import admin
from django.urls import path, include

from apps.treatment.views import RegisterTreatment, AddTreatmentView, ListTreatmentView, UpdateTreatmentView, \
    DeleteTreatmenView, QuotesPatients, ListStatusQuotesView, ChangeStatusQuotesView, PrescriptionView, PrescriptionPDF, \
    ListPrescriptionView, ChangePrescriptionView

urlpatterns = [
    path('agregar-tratamiento/', RegisterTreatment.as_view(), name='add_treatment'),
    path('generar-receta/', PrescriptionView.as_view(), name='add_prescription'),
    path('nuevo-tratamiento/', AddTreatmentView.as_view(), name='new_treatment'),
    path('lista-tratamiento/', ListTreatmentView.as_view(), name='list_treatment'),
    path('actualizar-tratamiento/<pk>', UpdateTreatmentView.as_view(), name='update_treatment'),
    path('eliminar-tratamiento/<pk>', DeleteTreatmenView.as_view(), name='delete_treatment'),
    path('agendar-cita/', QuotesPatients.as_view(), name='add_quotes'),
    path('listado-citas/', ListStatusQuotesView.as_view(), name='list_quotes'),
    path('actualizar-citas/<pk>', ChangeStatusQuotesView.as_view(), name='update_quotes'),
    path('actualizar-receta/<pk>', ChangePrescriptionView.as_view(), name='update_prescription'),
    path('listado-recetas/', ListPrescriptionView.as_view(), name='list_prescription'),
    # PDF
    path('generar-receta-pdf/<pk>', PrescriptionPDF.as_view(), name='prescription_pdf'),
]
