from django.core import validators
from django.db import models

from fruitipedia.validators import start_with_letter_validator


# Create your models here.

class Profile(models.Model):
    first_name = models.CharField(
        verbose_name='First Name',
        null=False,
        blank=False,
        max_length=25,
        validators=[
            validators.MinLengthValidator(2),
            start_with_letter_validator
        ]
    )

    last_name = models.CharField(
        verbose_name='Last Name',
        null=False,
        blank=False,
        max_length=35,
        validators=[
            validators.MinLengthValidator(1),
            start_with_letter_validator
        ]
    )

    email = models.EmailField(
        verbose_name='Email',
        null=False,
        blank=False,
        max_length=40
    )

    password = models.CharField(
        verbose_name='Password',
        null=False,
        blank=False,
        max_length=20,
        validators=[
            validators.MinLengthValidator(8),
        ]
    )

    image_url = models.URLField(
        verbose_name='Image URL',
        null=True,
        blank=True
    )

    age = models.IntegerField(
        verbose_name='Age',
        null=True,
        blank=True,
        default=18
    )
