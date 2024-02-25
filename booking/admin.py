from django.contrib import admin
from .models import Booking
from allauth.socialaccount.models import SocialToken, SocialAccount, SocialApp


# Register your models here.
@admin.register(Booking)
class AdminBooking(admin.ModelAdmin):
    """
    Display booking fields in admin panel
    """
    list_display = (
        'status', 'first_name', 'last_name',
        'email', 'number_of_people',
        'date', 'time', 'date_of_request',
        )
    list_filter = ('first_name', 'date', 'time', 'date_of_request',)


admin.site.unregister(SocialToken)
admin.site.unregister(SocialAccount)
admin.site.unregister(SocialApp)
