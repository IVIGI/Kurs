from .models import Hotel
from django import forms

class HotelForm(forms.ModelForm):
    class Meta:
        model = Hotel
        fields = ['Booked']
        widgets = {
            'Booked': forms.CheckboxInput(attrs={'id': 'booked-checkbox'})
        }