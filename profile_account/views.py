from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import EditForm, EditBookingForm
from booking.models import Booking


# Create your views here.
def profile_account(request):
    """
    Renders user profile template with user bookings and details
    """
    if request.user.is_authenticated:
        firstname = request.user.first_name
        lastname = request.user.last_name
        username = request.user.username
        emailaddress = request.user.email

        user_bookings = Booking.objects.filter(
            user=request.user).order_by('date', 'time')

        print(user_bookings)

        context = {
            'firstname': firstname,
            'lastname': lastname,
            'username': username,
            'emailaddress': emailaddress,
            'user_bookings': user_bookings
        }
        return render(request, 'accounts/profile.html', context)


@login_required
def delete_account(request):
    """
    Delete user account
    """
    if request.method == 'POST':
        user = request.user
        user.delete()
        messages.success(
            request,
            'Your account has been deleted successfully.'
        )
        return redirect('home')
    else:
        return render(request, 'accounts/delete_account.html')


@login_required
def edit_details(request):
    """
    Edit user account details
    """
    user = request.user

    if request.method == 'POST':
        edit_form = EditForm(request.POST, instance=user)

        if edit_form.is_valid():
            edit_form.save()
            update_bookings(user)
            messages.success(
                request,
                'Your account details were updated successfully!'
            )
            return redirect('profile_account')
    else:
        edit_form = EditForm(instance=user)

    return render(
        request,
        'accounts/edit_details.html',
        {'edit_form': edit_form}
    )


def update_bookings(user):
    """
    Validate user bookings to new user details
    """
    bookings = Booking.objects.filter(user=user)

    for booking in bookings:
        booking.first_name = user.first_name
        booking.last_name = user.last_name
        booking.username = user.username
        booking.email = user.email
        booking.save()


@login_required
def edit_booking(request, booking_id):
    """
    Edit specific user booking
    Validating that the booking doesn't already exist
    """
    booking = get_object_or_404(Booking, id=booking_id)

    if request.method == 'POST':
        form = EditBookingForm(request.POST, instance=booking)

        if form.is_valid():
            edited_booking = form.save(commit=False)
            existing_booking = Booking.objects.filter(
                user=request.user,
                date=edited_booking.date,
                time=edited_booking.time
            ).exclude(id=booking_id).first()

            if existing_booking:
                messages.error(
                    request,
                    'You already have a booking with the same date and time.'
                )
                return render(
                    request,
                    'accounts/edit_booking.html',
                    {'form': form}
                )

            edited_booking.save()
            messages.success(
                request,
                'Your booking has been updated successfully!'
            )
            return redirect('profile_account')
    else:
        form = EditBookingForm(instance=booking)

    return render(request, 'accounts/edit_booking.html', {'form': form})


@login_required
def delete_booking(request, booking_id):
    """
    Delete specific user booking
    """
    booking = get_object_or_404(Booking, id=booking_id)

    if request.method == 'POST':
        if booking.user == request.user:
            booking.delete()
            messages.success(
                request,
                'Your booking has been deleted successfully.'
            )
        else:
            messages.error(
                request,
                'You are not authorized to delete this booking.'
            )
        return redirect('profile_account')
    else:
        return render(request, 'accounts/delete_booking.html')
