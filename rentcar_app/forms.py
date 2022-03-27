from django import forms
from django.http import request

from rentcar_app.models import Rent


class DateInput(forms.DateInput):
    input_type = 'date'


class RentCarForm(forms.ModelForm):
    class Meta:
        model = Rent
        fields = '__all__'
        widgets = {
            'start_date': DateInput(),
            'end_date': DateInput(),
        }

