from django.db import models

from apps.patient.choices import GenderChoices


class Patients(models.Model):
    first_name = models.CharField(
        max_length=200,
        verbose_name="Nombres",
    )
    last_name = models.CharField(
        max_length=200,
        verbose_name="Apellidos",
    )
    direction = models.CharField(
        max_length=250,
        verbose_name="Dirección",
        default=""
    )
    identification = models.CharField(
        max_length=11,
        verbose_name="Cedula",
        unique=True
    )
    gender = models.CharField(
        choices=GenderChoices.choices,
        default=GenderChoices.male,
        max_length=100,
        verbose_name="Genero"
    )

    class Meta:
        verbose_name = "Paciente"
        verbose_name_plural = "Pacientes"

    def __str__(self):
        return self.first_name + " " + self.last_name
