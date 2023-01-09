from django.db import models

from apps.patient.models import Patients
from apps.treatment.choices import StatusQuotesChoices
from ckeditor.fields import RichTextField

class Treatment(models.Model):
    detail = models.CharField(
        max_length=100,
        verbose_name="Tipo de tratamiento"
    )
    price = models.DecimalField(
        max_digits=5,
        decimal_places=2,
        verbose_name='Precio'
    )
    patient = models.ManyToManyField(
        Patients,
        through="TreatmentPatient",
        blank=True,
        null=True,
    )

    class Meta:
        verbose_name = 'Tratamiento'
        verbose_name_plural = "Tratamientos"

    def __str__(self):
        return self.detail


class TreatmentPatient(models.Model):
    patient = models.ForeignKey(
        Patients,
        on_delete=models.PROTECT,
        verbose_name="Paciente"
    )
    treatment = models.ForeignKey(
        Treatment,
        on_delete=models.PROTECT,
        verbose_name="Tratamiento"
    )

    class Meta:
        verbose_name = 'Tratamiento Paciente'
        verbose_name_plural = "Tratamientos Pacientes"

    def __str__(self):
        _list = [
            str(self.patient),
            str(self.treatment),
        ]
        return str(_list)


class QuotesPatient(models.Model):
    date_hour = models.DateTimeField(
        verbose_name='Hora'
    )
    patient = models.ForeignKey(
        Patients,
        on_delete=models.PROTECT,
        verbose_name="Paciente"
    )

    status_quotes = models.CharField(
        verbose_name='Estado de la cita',
        choices=StatusQuotesChoices.choices,
        default=StatusQuotesChoices.PENDING,
        max_length=100,
    )

    class Meta:
        verbose_name = 'Cita'
        verbose_name_plural = 'Citas'

    def __str__(self):
        return str(self.date_hour) + "-" + str(self.patient) + "-" + str(self.status_quotes)


class Prescription(models.Model):
    patient = models.ForeignKey(
        Patients,
        on_delete=models.PROTECT,
        verbose_name='Paciente'
    )
    prescription = RichTextField(
        verbose_name='Prescripcion de la receta medica'
    )

    date = models.DateTimeField(auto_now=True,auto_created=True)

    class Meta:
        ordering = ['-patient']
        verbose_name = 'Receta'
        verbose_name_plural = 'Recetas'

    def __str__(self):
        list_prescription = [
            str(self.patient),
            str(self.prescription),
        ]
        return str(list_prescription)



