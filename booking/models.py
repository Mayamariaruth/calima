from django.db import models
from django.contrib.auth.models import User


# Create your models here.
available_times = [
    ('10:00', '10:00 AM'),
    ('11:00', '11:00 AM'),
    ('12:00', '12:00 PM'),
    ('13:00', '1:00 PM'),
    ('14:00', '2:00 PM'),
    ('15:00', '3:00 PM'),
    ('16:00', '4:00 PM'),
    ('17:00', '5:00 PM'),
    ('18:00', '6:00 PM'),
    ('19:00', '7:00 PM'),
    ('20:00', '8:00 PM'),
    ('21:00', '9:00 PM'),
    ('22:00', '10:00 PM'),
]


class Booking(models.Model):
    """
    Booking tables model
    """
    booking_status = [
        ('pending', 'pending'),
        ('approved', 'approved'),
        ('denied', 'denied'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    number_of_people = models.IntegerField()
    date = models.DateField()
    time = models.CharField(max_length=5, choices=available_times)
    special_requests = models.CharField(max_length=500, blank=True)
    date_of_request = models.DateTimeField(auto_now_add=True)
    status = models.CharField(
        max_length=10, choices=booking_status, default="pending"
        )

    def __str__(self):
        return f"{self.user} - {self.date} {self.time} / {self.status}"
