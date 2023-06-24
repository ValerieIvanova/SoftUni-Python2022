from django.core import validators
from django.db import models

from car_collection.car.validators import valid_car_year


# Create your models here.


class Car(models.Model):
    CHOICES = (
        ('Sports Car', 'Sports Car'),
        ('Pickup', 'Pickup'),
        ('Crossover', 'Crossover'),
        ('Minibus', 'Minibus'),
        ('Other', 'Other'),
    )
    type = models.CharField(
        max_length=10,
        choices=CHOICES,
        null=False,
        blank=False
    )

    model = models.CharField(
        max_length=20,
        validators=[validators.MinLengthValidator(2)],
        null=False,
        blank=False
    )

    year = models.IntegerField(
        null=False,
        blank=False,
        validators=[valid_car_year]
    )

    image_url = models.URLField(
        blank=False,
        null=False,
    )

    price = models.FloatField(
        null=False,
        blank=False,
        validators=[validators.MinValueValidator(1)],
    )

