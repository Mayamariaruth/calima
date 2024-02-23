from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from booking.models import Booking
from .forms import EditForm


# Create your views here.
def profile_account(request):
    if request.user.is_authenticated:
        firstname = request.user.first_name
        lastname = request.user.last_name
        username = request.user.username
        emailaddress = request.user.email

        user_bookings = Booking.objects.filter(user=request.user).order_by('-date', '-time')

        context = {
            'firstname': firstname,
            'lastname': lastname,
            'username': username,
            'emailaddress': emailaddress,
            'user_bookings': user_bookings
        }
        return render(request, 'accounts/profile.html', context)


def delete_account(request):
    return render(request, 'accounts/delete_account.html')


def edit_details(request):
    if request.method == 'POST':
        edit_form = EditForm(request.POST, instance=request.user)

        if edit_form.is_valid():
            edit_form.save()
            messages.success(request, 'Your account details were updated successfully!')
            return redirect('profile_account')
    else:
        edit_form = EditForm(instance=request.user)

    return render(request, 'accounts/edit_details.html', {'edit_form': edit_form,})
