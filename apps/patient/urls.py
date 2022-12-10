from django.contrib import admin
from django.urls import path

from apps.patient.views import HomePageView, ListPatientsView, AddPatientsView, UpdatePatientView, DeletePatientView

urlpatterns = [
    path('', HomePageView.as_view(),name='home'),
    path('lista-paciente/', ListPatientsView.as_view(),name='list_patients'),
    path('agregar-paciente/', AddPatientsView.as_view(),name='add_patients'),
    path('actualizar-paciente/<pk>', UpdatePatientView.as_view(),name='update_patients'),
    path('eliminar-paciente/<pk>', DeletePatientView.as_view(),name='delete_patients'),
]
