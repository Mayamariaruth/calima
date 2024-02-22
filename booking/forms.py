import datetime
from .models import Booking, available_times
from django import forms
from django.core.validators import MinValueValidator, MaxValueValidator


# Create your forms here.
class BookingForm(forms.ModelForm):
    """
    Booking form
    """
    class Meta:
        model = Booking
        fields = ('first_name', 'last_name', 'email', 'date', 'time', 'number_of_people',)

        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'}),
            'time': forms.Select(choices=available_times),
        }
        validators = {
            'number_of_people': [MinValueValidator(1), MaxValueValidator(6)],
            'date': [MinValueValidator(datetime.date.today)]
        }
