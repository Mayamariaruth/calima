from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import BookingForm


# Create your views here.
@login_required
def book_table(request):
    """
    Creates a user request for a table booking
    """
    heading = 'Book a table'

    if request.method == "POST":
        form = BookingForm(data=request.POST)

        if form.is_valid():
            booking = form.save(commit=False)
            booking.user = request.user
            booking.save()
            return render(request, 'booking/booking_success.html')
        else:
            messages.error(request, 'Please correct the errors below and try again.')
            return render(request, 'booking/booking_form.html', {'form': form})
    else:
        booking_form = BookingForm(initial={
            'first_name': request.user.first_name,
            'last_name': request.user.last_name,
            'email': request.user.email
        })

        return render(
            request,
            'booking/booking_form.html',
            {'form': booking_form, 'heading': heading}
        )


def booking_success(request):
    return render(request, 'booking/booking_success.html')
