from django.db.models import Q
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, UpdateView, DeleteView

from apps.treatment.forms import NewTreatmentForm, AddTreatmentForm
from apps.treatment.models import Treatment, TreatmentPatient


class RegisterTreatment(CreateView):
    model = Treatment
    form_class = NewTreatmentForm
    template_name = 'add_trearment.html'
    success_url = reverse_lazy('list_patients')

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['title'] = 'Agregar nuevo tratamiento'
        return context


class AddTreatmentView(CreateView):
    model = Treatment
    form_class = AddTreatmentForm
    template_name = 'add_trearment.html'
    success_url = reverse_lazy('list_treatment')

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['title'] = 'Iniciar tratamiento'
        return context


class UpdateTreatmentView(UpdateView):
    model = TreatmentPatient
    form_class = AddTreatmentForm
    template_name = 'update_treatment.html'
    success_url = reverse_lazy('list_treatment')

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['title'] = 'Actualizar tratamiento'
        return context


class DeleteTreatmenView(DeleteView):
    model = TreatmentPatient
    template_name = 'delete_treatment.html'
    success_url = reverse_lazy('list_treatment')


class ListTreatmentView(ListView):
    model = TreatmentPatient
    template_name = 'list_treatment.html'

    def get_queryset(self):
        search_patient = self.request.GET.get('paciente', '')
        lista_patient = TreatmentPatient.objects.filter(
            Q(patient__first_name__icontains=search_patient) | Q(patient__last_name__icontains=search_patient) |
            Q(patient__identification__icontains=search_patient)
        )
        return lista_patient

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['title'] = 'Lista de tratamientos'
        return context
