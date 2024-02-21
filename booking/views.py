from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Booking
from .forms import BookingForm

# Create your views here.
def book_table(request):
    """
    Creates a user request for a table booking
    """
    if request.method == "POST" and request.user.is_authenticated:
        heading = 'Book a table'
        booking_form = BookingForm(data=request.POST)

        if booking_form.is_valid():
            form = booking_form.save()
            form.author = request.user
            form.save()
            return render(request, 'booking_success')
        else:
            messages.info(
            request,
            ("Please login/signup as a customer to book a table!")
            )
    else:
        booking_form = BookingForm()

    return render(request, 'booking/booking_form.html', {'form': booking_form})


def booking_success(request):
    return render(request, 'booking/booking_success.html')
