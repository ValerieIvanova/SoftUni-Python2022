from django.core import validators
from django.db import models

from my_music_app.profileApp.validators import alnum_underscore_validator


# Create your models here.
class Profile(models.Model):
    username = models.CharField(
        null=False,
        blank=False,
        max_length=15,
        validators=[
            validators.MinLengthValidator(2),
            alnum_underscore_validator
        ]
    )
    email = models.EmailField(
        null=False,
        blank=False,
    )

    age = models.PositiveIntegerField(
        null=True,
        blank=True
    )

