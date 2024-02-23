from django.shortcuts import render
from django.contrib import messages
from .forms import BookingForm
from django.contrib.auth.models import User


# Create your views here.
def book_table(request):
    """
    Creates a user request for a table booking
    """
    heading = 'Book a table'

    if request.method == "POST" and request.user.is_authenticated:
        booking_form = BookingForm(data=request.POST)

        if booking_form.is_valid():
            form = booking_form.save(commit=False)
            form.author = request.user
            form.save()
            return render(request, 'booking/booking_success.html')
    else:
        messages.info(
                request,
                ("Please login/signup as a customer to book a table!")
            )
    
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
