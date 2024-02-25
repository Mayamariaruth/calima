from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import BookingForm
from .models import Booking


# Create your views here.
@login_required
def book_table(request):
    """
    Creates a user request for a table booking.
    Validates that an identical booking doesn't already exist
    and that you can't book same-day bookings
    """
    if request.method == "POST":
        form = BookingForm(data=request.POST)

        if form.is_valid():
            booking = form.save(commit=False)
            booking.user = request.user
            
            if Booking.objects.filter(
                user=booking.user,
                date=booking.date,
                time=booking.time,
            ).exists():
                messages.error(request, 'You already have a booking with the same date and time.')
                return render(request, 'booking/booking_form.html', {'form': form})
            else:
                booking.save()
                messages.success(request, 'Booking successful!')
                return render(request, 'booking/booking_success.html')
        else:
            return render(request, 'booking/booking_form.html', {'form': form})
    else:
        form = BookingForm(initial={
            'first_name': request.user.first_name,
            'last_name': request.user.last_name,
            'email': request.user.email
        })

        return render(
            request,
            'booking/booking_form.html',
            {'form': form}
        )


def booking_success(request):
    return render(request, 'booking/booking_success.html')
