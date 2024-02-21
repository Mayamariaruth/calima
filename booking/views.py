from django.shortcuts import render, redirect
from booking.models import Booking
from booking.forms import BookingForm

# Create your views here.
def book_table(request):
    """
    Creates a user request for a table booking
    """
    return render(request, 'booking/booking_form.html')

    if request.method == "POST" and request.user.is_authenticated:
        heading = 'Book a table'
        form = BookingForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'booking_success')
        else:
            messages.info(
            request,
            ("Please login/signup as a customer to book a table!")
            )
    else:
        form = BookingForm()


def booking_success(request):
    return render(request, 'booking/booking_success.html')