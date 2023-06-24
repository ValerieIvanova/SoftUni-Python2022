from django.core import validators
from django.db import models


# Create your models here.

class Album(models.Model):
    CHOICES = (
        ('Pop Music', 'Pop Music'),
        ('Jazz Music', 'Jazz Music'),
        ('R&B Music', 'R&B Music'),
        ('Rock Music', 'Rock Music'),
        ('Country Music', 'Country Music'),
        ('Dance Music', 'Dance Music'),
        ('Hip-Hop Music', 'Hip-Hop Music'),
        ('Other', 'Other'),
    )

    album_name = models.CharField(
        null=False,
        blank=False,
        max_length=30,
        unique=True,
        verbose_name='Album Name'
    )

    artist = models.CharField(
        null=False,
        blank=False,
        max_length=30
    )

    genre = models.CharField(
        null=False,
        blank=False,
        max_length=30,
        choices=CHOICES
    )

    description = models.TextField(
        null=True,
        blank=True
    )

    image_url = models.URLField(
        null=False,
        blank=False,
        verbose_name='Image URL'
    )

    price = models.FloatField(
        null=False,
        blank=False,
        validators=[
            validators.MinValueValidator(0.0)
        ]
    )
