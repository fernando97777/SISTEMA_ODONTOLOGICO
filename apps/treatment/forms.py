from django import forms

from apps.treatment.models import Treatment, TreatmentPatient


class NewTreatmentForm(forms.ModelForm):
    class Meta:
        model = Treatment
        fields = "__all__"
        exclude = ['patient']
        widgets = {
            'detail': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'style': 'margin-top: 5px; margin-bottom: 10px;'
                }
            ),
            'price': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'style': 'margin-top: 5px; margin-bottom: 10px;'
                }
            ),
        }


class AddTreatmentForm(forms.ModelForm):
    class Meta:
        model = TreatmentPatient
        fields = "__all__"
        widgets = {
            'patient': forms.Select(
                attrs={
                    'class': 'form-control',
                    'style': 'margin-top: 5px; margin-bottom: 10px;'
                }
            ),
            'treatment': forms.Select(
                attrs={
                    'class': 'form-control',
                    'style': 'margin-top: 5px; margin-bottom: 10px;'
                }
            ),
        }
