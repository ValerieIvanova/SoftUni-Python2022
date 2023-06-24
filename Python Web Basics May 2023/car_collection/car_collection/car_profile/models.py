from django.core.validators import MinLengthValidator, MinValueValidator
from django.db import models


# Create your models here.


class Profile(models.Model):
    username = models.CharField(
        max_length=10,
        null=False,
        blank=False,
        validators=[
            MinLengthValidator(2, 'The username must be a minimum of 2 chars'),
        ])

    email = models.EmailField(
        null=False,
        blank=False,
    )

    age = models.PositiveIntegerField(
        null=False,
        blank=False,
        validators=[MinValueValidator(18)],
    )

    password = models.CharField(
        max_length=30,
        null=False,
        blank=False,
    )

    first_name = models.CharField(
        max_length=30,
        null=True,
        blank=True,
    )

    last_name = models.CharField(
        max_length=30,
        null=True,
        blank=True
    )

    profile_picture = models.URLField(
        null=True,
        blank=True
    )
