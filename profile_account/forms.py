from django import forms
from django.contrib.auth.models import User
from booking.models import Booking


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
