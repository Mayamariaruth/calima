from django.shortcuts import render, redirect
from booking.models import Booking
from booking.forms import BookingForm

# Create your views here.
def book_table(request):
    """
    Creates a user request for a table booking
    """
    if request.method == "POST" and request.user.is_authenticated:
        heading = 'Book a table'
        form = BookingForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('booking_success')
        else:
            messages.info(
            request,
            ("Please login/signup as a customer to book a table!")
            )
    else:
        form = BookingForm()

    return render(request, 'booking_form.html', {'form': form})


def booking_success(request):
    """
    Render booking success html
    """
    return render(request, 'booking_success.html')