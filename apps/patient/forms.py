from django import forms

from apps.patient.models import Patients


class AddPatientsForm(forms.ModelForm):
    class Meta:
        model = Patients
        fields = '__all__'
        widgets = {
            'first_name': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'style': 'margin-top: 5px;'
                }
            ),
            'last_name': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'style': 'margin-top: 5px;'
                }
            ),
            'direction': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'style': 'margin-top: 5px;'
                }
            ),
            'identification': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'style': 'margin-top: 5px;'
                }
            )
            ,
            'gender': forms.Select(
                attrs={
                    'class': 'form-control',
                    'style': 'margin-top: 5px;'
                }
            ),
        }
