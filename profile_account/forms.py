import datetime
from django import forms
from django.contrib.auth.models import User
from booking.models import Booking, available_times


# Create your forms here.
class EditForm(forms.ModelForm):
    """
    Edit account details form
    """
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username', 'email',)
        help_texts = {
            'username': 'Required. Letters, digits and @/./+/-/_ only.',
            'email': 'Required. Letters, digits and @/./+/-/_ only.'
        }

    def clean(self):
        cleaned_data = super().clean()
        username = self.cleaned_data.get('username')
        email = self.cleaned_data.get('email')

        instance = self.instance

        if username and username != instance.username:
            if User.objects.filter(username=username).exists():
                self.add_error('username', 'This username is already in use.')
        if email and email != instance.email:
            if User.objects.filter(email=email).exists():
                self.add_error('email', 'This email is already in use.')

        return cleaned_data


class EditBookingForm(forms.ModelForm):
    """
    Edit booking requests form
    """
    class Meta:
        model = Booking
        fields = ('date', 'time', 'number_of_people', 'special_requests',)

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
