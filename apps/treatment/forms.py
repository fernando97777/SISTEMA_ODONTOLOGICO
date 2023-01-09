from django import forms

from apps.treatment.models import Treatment, TreatmentPatient, QuotesPatient


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


class QuotesPatientsForms(forms.ModelForm):
    date_hour = forms.DateTimeField(
        label="Data/hora",
        widget=forms.DateTimeInput(
            format='%Y-%m-%dT%H:%M',
            attrs={
                'type': 'datetime-local'
            }),
        input_formats=('%Y-%m-%dT%H:%M',),
    )

    class Meta:
        model = QuotesPatient
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(QuotesPatientsForms, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'
