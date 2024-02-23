import datetime
from .models import Booking, available_times
from django import forms


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
        Validation for the date field
        """
        date = self.cleaned_data['date']

        if date < datetime.date.today():
            raise forms.ValidationError("Booking date cannot be in the past.")
        return date

    def clean_number_of_people(self):
        """
        Validation for the number_of_people field
        """
        number_of_people = self.cleaned_data['number_of_people']

        if number_of_people < 1:
            raise forms.ValidationError("Number of people must be at least 1.")
        elif number_of_people > 6:
            raise forms.ValidationError("Number of people cannot exceed 6.")
        return number_of_people
