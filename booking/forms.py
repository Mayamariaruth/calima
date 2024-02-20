from .models import Booking
from django import forms


# Create your forms here.
class BookingForm(forms.ModelForm):
    """
    Booking form
    """
    class Meta:
        model = Booking
        fields = ('date', 'time', 'number_of_people',)
