# Generated by Django 5.0.2 on 2024-02-22 03:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='booking',
            name='status',
            field=models.CharField(choices=[('pending', 'pending'), ('approved', 'approved'), ('denied', 'denied')], default='pending', max_length=10),
        ),
        migrations.AlterField(
            model_name='booking',
            name='time',
            field=models.CharField(choices=[('09:00', '9:00 AM'), ('10:00', '10:00 AM'), ('11:00', '11:00 AM'), ('12:00', '12:00 PM'), ('13:00', '1:00 PM'), ('14:00', '2:00 PM'), ('15:00', '3:00 PM'), ('16:00', '4:00 PM'), ('17:00', '5:00 PM'), ('18:00', '6:00 PM'), ('19:00', '7:00 PM'), ('20:00', '8:00 PM')], max_length=5),
        ),
    ]
