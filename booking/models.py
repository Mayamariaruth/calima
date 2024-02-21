import datetime
from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator


# Create your models here.
available_times = (
    ('9:00 AM', '9:00 AM'),
    ('10:00 AM', '10:00 AM'),
    ('11:00 AM', '11:00 AM'),
    ('12:00 PM', '12:00 PM'),
    ('1:00 PM', '1:00 PM'),
    ('2:00 PM', '2:00 PM'),
    ('3:00 PM', '3:00 PM'),
    ('4:00 PM', '4:00 PM'),
    ('5:00 PM', '5:00 PM'),
    ('6:00 PM', '6:00 PM'),
    ('7:00 PM', '7:00 PM'),
    ('8:00 PM', '8:00 PM'),
)


class Booking(models.Model):
    """
    Booking tables model
    """
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    number_of_people = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(6)])
    date = models.DateField(validators=[MinValueValidator(datetime.date.today)])
    time = models.TimeField(choices=available_times)
    date_of_request = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
