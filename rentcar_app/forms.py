from django import forms
from rentcar_app.models import Rent


class RentEditForm(forms.ModelForm):   # Form which allows to edit reservations
    class Meta:
        model = Rent
        exclude = ['user', 'car']
        widgets = {
            'start_date': forms.DateInput(attrs={'type': 'date'}),
            'end_date': forms.DateInput(attrs={'type': 'date'}),
        }
