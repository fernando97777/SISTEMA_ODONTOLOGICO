from django.db import models


class GenderChoices(models.TextChoices):
    female = "FEMENINO","FEMENINO"
    male = "MASCULINO","MASCULINO"
