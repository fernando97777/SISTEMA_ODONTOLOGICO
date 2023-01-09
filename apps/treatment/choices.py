from django.db import models


class TreatmentPatientChoices(models.TextChoices):
    calzaDiente = "CALZA DE DIENTE", "CALZA DE DIENTE"
    brackets = "BRACKETS", "BRACKETS"


class StatusQuotesChoices(models.TextChoices):
    PENDING = "PENDIENTE", "PENDIENTE"
    CANCELLED = "CANCELADO", "CANCELADO"
    COMPLETE = "COMPLETADO", "COMPLETADO"
