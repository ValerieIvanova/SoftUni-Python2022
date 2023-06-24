from django.core import validators
from django.db import models

from fruitipedia.validators import contains_only_letters_validator


# Create your models here.

class Fruit(models.Model):
    name = models.CharField(
        verbose_name="Name",
        null=False,
        blank=False,
        max_length=30,
        validators=[
            validators.MinLengthValidator(2),
            contains_only_letters_validator
        ]
    )

    image_url = models.URLField(
        verbose_name="Image URL",
        null=False,
        blank=False,
    )

    description = models.TextField(
        verbose_name="Description",
        null=False,
        blank=False
    )

    nutrition = models.TextField(
        verbose_name="Nutrition",
        null=True,
        blank=True
    )
