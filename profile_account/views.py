from django.shortcuts import render
from django.contrib.auth.models import User
from booking.models import Booking


# Create your views here.
def profile_account(request):
    if request.user.is_authenticated and not request.user.is_staff:
        firstname = request.user.first_name
        lastname = request.user.last_name
        username = request.user.username
        emailaddress = request.user.email

        user_bookings = Booking.objects.all().values()

        context = {
            'firstname': firstname,
            'lastname': lastname,
            'username': username,
            'emailaddress': emailaddress,
            'user_bookings': user_bookings
        }
        return render(request, 'profiles/profile.html', context)
