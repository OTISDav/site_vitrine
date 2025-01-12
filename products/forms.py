from django import forms
from .models import Appointment

class AppointmentForm(forms.ModelForm):
    class Meta:
        model = Appointment
        fields = ['name', 'email', 'date', 'time']
        widgets = {
            'date': forms.TextInput(attrs={
                'id': 'date',
                'placeholder': 'Choisissez une date'
            }),
            'time': forms.TextInput(attrs={
                'id': 'time',
                'placeholder': 'Choisissez une heure'
            }),
        }
