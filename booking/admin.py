from django.contrib import admin
from .models import Booking


# Register your models here.
@admin.register(Booking)
class AdminBooking(admin.ModelAdmin):
    """
    Display bookings in admin panel
    """
    list_display = ('user', 'first_name', 'last_name', 'email', 'number_of_people', 'date', 'time', 'date_of_request',)
    list_filter = ('user', 'date', 'time',)
