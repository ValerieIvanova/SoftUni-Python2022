from django.core import validators
from django.db import models

from my_plant_app.validators import capital_letter_validator


# Create your models here.


class Profile(models.Model):
    username = models.CharField(
        null=False,
        blank=False,
        max_length=10,
        validators=[
            validators.MinLengthValidator(2)
        ]
    )

    first_name = models.CharField(
        null=False,
        blank=False,
        max_length=20,
        validators=[
            capital_letter_validator
        ]
    )

    last_name = models.CharField(
        null=False,
        blank=False,
        max_length=20,
        validators=[
            capital_letter_validator
        ]
    )

    profile_picture = models.URLField(
        null=True,
        blank=True,
    )

