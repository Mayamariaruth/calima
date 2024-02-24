from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.models import User
from booking.models import Booking
from .forms import EditForm


# Create your views here.
def profile_account(request):
    if request.user.is_authenticated:
        firstname = request.user.first_name
        lastname = request.user.last_name
        username = request.user.username
        emailaddress = request.user.email

        user_bookings = Booking.objects.filter(
            user=request.user).order_by('-date', '-time')

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
        messages.success(request, 'Your account has been deleted successfully.')
        return redirect('home')
    else:
        return render(request, 'accounts/delete_account.html')


@login_required
def edit_details(request):
    """
    Edit user account details
    """
    user = get_object_or_404(request.user)

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
