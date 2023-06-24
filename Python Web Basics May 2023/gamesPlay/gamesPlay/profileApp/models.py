from django.core import validators
from django.db import models


# Create your models here.
class Profile(models.Model):
    email = models.EmailField(
        null=False,
        blank=False
    )

    age = models.IntegerField(
        null=False,
        blank=False,
        validators=[
            validators.MinValueValidator(12),
        ]
    )

    password = models.CharField(
        null=False,
        blank=False,
        max_length=30,

    )

    first_name = models.CharField(
        null=True,
        blank=True,
        max_length=30
    )

    last_name = models.CharField(
        null=True,
        blank=True,
        max_length=30
    )

    profile_picture = models.URLField(
        null=True,
        blank=True
    )
