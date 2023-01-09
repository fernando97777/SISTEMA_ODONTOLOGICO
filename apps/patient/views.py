from django.db.models import Q
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, UpdateView, DeleteView

from apps.patient.forms import AddPatientsForm
from apps.patient.models import Patients
from apps.treatment.models import QuotesPatient, TreatmentPatient


class HomePageView(ListView):
    model = QuotesPatient
    template_name = 'list_quote.html'

    def get_queryset(self):
        search_patient = self.request.GET.get('paciente', '')
        lista_patient = QuotesPatient.objects.filter(
            Q(patient__first_name__icontains=search_patient) | Q(patient__last_name__icontains=search_patient) |
            Q(patient__identification__icontains=search_patient)
        )
        return lista_patient

    def get_context_data(self, *args, **kwargs):
        cita = QuotesPatient.objects.filter(
            status_quotes__icontains="PENDIENTE"
        ).count()
        patients = Patients.objects.all().count()
        treatment = TreatmentPatient.objects.all().count()

        context = super().get_context_data()
        context['patient_number'] = patients
        context['quotes_number'] = cita
        context['treatment_number'] = treatment
        context['title'] = 'Citas Pendientes'
        context['user'] = self.request.user
        return context


class ListPatientsView(ListView):
    model = Patients
    template_name = 'list_patients.html'

    def get_context_data(self, *args, **kwargs):
        context = super(ListPatientsView, self).get_context_data()
        context['title'] = "Listado de pacientes"
        context['gender'] = Patients.objects.all()
        return context


class AddPatientsView(CreateView):
    model = Patients
    template_name = 'add_patients.html'
    form_class = AddPatientsForm
    success_url = reverse_lazy('list_patients')

    def get_context_data(self, *args, **kwargs):
        context = super(AddPatientsView, self).get_context_data()
        context['title'] = "Agregar nuevo paciente"
        return context


class UpdatePatientView(UpdateView):
    model = Patients
    template_name = 'update_patients.html'
    form_class = AddPatientsForm
    success_url = reverse_lazy('list_patients')

    def get_context_data(self, *args, **kwargs):
        context = super(UpdatePatientView, self).get_context_data()
        context['title'] = "Actualizar información del paciente"
        return context


class DeletePatientView(DeleteView):
    model = Patients
    template_name = 'delete_patient.html'
    success_url = reverse_lazy('list_patients')
