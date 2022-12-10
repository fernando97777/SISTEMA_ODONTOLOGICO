from django.db import models

from apps.patient.models import Patients
from apps.treatment.choices import TreatmentPatientChoices


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
