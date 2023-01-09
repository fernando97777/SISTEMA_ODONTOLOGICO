from django.db.models import Q
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, UpdateView, DeleteView, View

from apps.patient.forms import AddPrescription
from apps.treatment.forms import NewTreatmentForm, AddTreatmentForm, QuotesPatientsForms
from apps.treatment.models import Treatment, TreatmentPatient, QuotesPatient, Prescription

# PDF
import os
from django.conf import settings
from django.http import HttpResponse
from django.template.loader import get_template
from xhtml2pdf import pisa
from django.contrib.staticfiles import finders


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


class QuotesPatients(CreateView):
    model = QuotesPatient
    form_class = QuotesPatientsForms
    template_name = 'add_quotes.html'
    success_url = reverse_lazy('home')

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['title'] = 'Agendar cita'
        return context


class ListQuotesView(ListView):
    model = QuotesPatient
    template_name = 'list_quote.html'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data()
        context['title'] = "Citas Pendientes"
        return context


class ListStatusQuotesView(ListView):
    model = QuotesPatient
    template_name = 'status_quotes.html'
    paginate_by = 6

    def get_queryset(self):
        search_quotes = self.request.GET.get('quote', '')
        status_quotes = QuotesPatient.objects.filter(
            Q(status_quotes__icontains=search_quotes)
        )
        return status_quotes

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data()
        context['title'] = "Historial de citas"
        return context


class ChangeStatusQuotesView(UpdateView):
    model = QuotesPatient
    form_class = QuotesPatientsForms
    template_name = 'update_status_quotes.html'
    success_url = reverse_lazy('home')

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data()
        context['title'] = "Actualizar Cita"
        return context


class PrescriptionView(CreateView):
    model = Prescription
    form_class = AddPrescription
    template_name = 'add_prescription.html'
    success_url = reverse_lazy('list_prescription')

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['title'] = 'Receta'
        return context


class PrescriptionPDF(View):
    def get(self, request, *args, **kwargs):
        template = get_template('pdf/prescription.html')
        data = Prescription.objects.get(pk=self.kwargs['pk'])
        context = {
            'patient': data.patient,
            'table': data.prescription,
            'date': data.date,
        }
        html = template.render(context)
        response = HttpResponse(content_type='application/pdf')
        response['Content-Disposition'] = f'attachment; filename="{data.patient}.pdf"'
        pisa_status = pisa.CreatePDF(
            html, dest=response)
        if pisa_status.err:
            return HttpResponse('Error' + html + '</pre>')
        return response


class ListPrescriptionView(ListView):
    model = Prescription
    template_name = 'list_prescription.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data()
        context['title'] = 'Historial de recetas'
        return context


class ChangePrescriptionView(UpdateView):
    model = Prescription
    form_class = AddPrescription
    template_name = 'add_prescription.html'
    success_url = reverse_lazy('home')

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data()
        context['title'] = "Actualizar Cita"
        return context
