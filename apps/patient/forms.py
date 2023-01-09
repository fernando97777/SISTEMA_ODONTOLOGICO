from django import forms
from apps.patient.models import Patients
from superadmin.forms import ModelForm

from apps.treatment.models import Prescription


class AddPatientsForm(ModelForm):
    class Meta:
        model = Patients
        fields = (("first_name","last_name"))


class AddPrescription(forms.ModelForm):
    class Meta:
        model = Prescription
        fields = "__all__"
        widgets = {
            'patient': forms.Select(
                attrs={
                    'class': 'form-control',
                    'style': 'margin-top: 5px; margin-bottom: 10px;'
                }
            ),
            'prescription': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'style': 'margin-top: 5px; margin-bottom: 10px;'
                }
            ),
        }

