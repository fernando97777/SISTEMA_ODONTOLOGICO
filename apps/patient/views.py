from django.db.models import Q
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import TemplateView, CreateView, ListView, UpdateView, DeleteView,DetailView

from apps.patient.forms import AddPatientsForm
from apps.patient.models import Patients


class HomePageView(ListView):
    model = Patients
    template_name = 'cards_info.html'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data()
        context['patient_number'] = Patients.objects.all().count()
        return context


class ListPatientsView(ListView):
    model = Patients
    template_name = 'list_patients.html'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data()
        context['title'] = "Listado de pacientes"
        context['gender'] = Patients.objects.all()
        return context


class AddPatientsView(CreateView):
    model = Patients
    template_name = 'add_patients.html'
    form_class = AddPatientsForm
    success_url = reverse_lazy('list_patients')

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data()
        context['title'] = "Agregar nuevo paciente"
        return context


class UpdatePatientView(UpdateView):
    model = Patients
    template_name = 'update_patients.html'
    form_class = AddPatientsForm
    success_url = reverse_lazy('list_patients')

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data()
        context['title'] = "Actualizar información del paciente"
        return context


class DeletePatientView(DeleteView):
    model = Patients
    template_name = 'delete_patient.html'
    success_url = reverse_lazy('list_patients')
