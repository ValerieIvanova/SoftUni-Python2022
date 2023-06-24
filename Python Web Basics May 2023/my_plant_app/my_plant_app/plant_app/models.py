from django.core import validators
from django.db import models
from my_plant_app.validators import all_letters_validator


# Create your models here.

class Plant(models.Model):
    CHOICES = (
        ('Outdoor Plants', 'Outdoor Plants'),
        ('Indoor Plants', 'Indoor Plants'),
    )

    plant_type = models.CharField(
        null=False,
        blank=False,
        max_length=14,
        choices=CHOICES
    )

    name = models.CharField(
        null=False,
        blank=False,
        max_length=20,
        validators=[
            validators.MinLengthValidator(2),
            all_letters_validator
        ]
    )

    image_url = models.URLField(
        null=False,
        blank=False
    )

    description = models.TextField(
        null=False,
        blank=False
    )

    price = models.FloatField(
        null=False,
        blank=False
    )
