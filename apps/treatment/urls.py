from django.contrib import admin
from django.urls import path, include

from apps.treatment.views import RegisterTreatment, AddTreatmentView, ListTreatmentView, UpdateTreatmentView, \
    DeleteTreatmenView

urlpatterns = [
    path('agregar-tratamiento/', RegisterTreatment.as_view(), name='add_treatment'),
    path('nuevo-tratamiento/', AddTreatmentView.as_view(), name='new_treatment'),
    path('lista-tratamiento/', ListTreatmentView.as_view(), name='list_treatment'),
    path('actualizar-tratamiento/<pk>', UpdateTreatmentView.as_view(), name='update_treatment'),
    path('eliminar-tratamiento/<pk>', DeleteTreatmenView.as_view(), name='delete_treatment')
]
