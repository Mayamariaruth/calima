from django.urls import path
from .views import book_table, booking_success


urlpatterns = [
    path('booking/book/', book_table, name='book_table'),
    path('booking/success/', booking_success, name='booking_success'),
]
