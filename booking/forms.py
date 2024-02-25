import datetime
from django.core.exceptions import ValidationError
from django import forms
from .models import Booking, available_times


# Create your forms here.
class BookingForm(forms.ModelForm):
    """
    Booking form
    """
    class Meta:
        model = Booking
        fields = (
            'first_name', 'last_name', 'email',
            'date', 'time', 'number_of_people',
            'special_requests',
            )

        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'}),
            'time': forms.Select(choices=available_times),
        }

    def clean_date(self):
        """
        Validating that the booking date is not in the past
        or the same day user is making the request
        """
        date = self.cleaned_data.get('date')

        if date == datetime.date.today():
            raise forms.ValidationError(
                "It is not possible to book same-day bookings."
            )
        elif date and date < datetime.date.today():
            raise forms.ValidationError("Booking date cannot be in the past.")

        return date

    def clean_number_of_people(self):
        """
        Validating that the number of people is between 1-6
        """
        number_of_people = self.cleaned_data.get('number_of_people')

        if number_of_people and (number_of_people < 1 or number_of_people > 6):
            raise forms.ValidationError(
                "Number of people must be between 1 and 6."
            )

        return number_of_people
