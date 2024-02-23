from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import BookingForm
from django.contrib.auth.models import User


# Create your views here.
def book_table(request):
    """
    Creates a user request for a table booking
    """
    heading = 'Book a table'

    if request.method == "POST":
        if request.user.is_authenticated:
            form = BookingForm(data=request.POST)

            if form.is_valid():
                booking = form.save(commit=False)
                booking.user = request.user
                booking.save()
                return render(request, 'booking/booking_success.html')
        else:
            messages.info(request, "Please login/signup as a customer to book a table!")
            return redirect('account_login')

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
