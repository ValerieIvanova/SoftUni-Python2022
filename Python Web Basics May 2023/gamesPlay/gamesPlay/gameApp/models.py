from django.core import validators
from django.db import models

from gamesPlay.gameApp.validators import rating_validator


# Create your models here.

class Game(models.Model):
    CHOICES = (
        ('Action', 'Action'),
        ('Adventure', 'Adventure'),
        ('Puzzle', 'Puzzle'),
        ('Strategy', 'Strategy'),
        ('Sports', 'Sports'),
        ('Board/Card Game', 'Board/Card Game'),
        ('Other', 'Other')
    )

    title = models.CharField(
        null=False,
        blank=False,
        max_length=30,
        unique=True
    )

    category = models.CharField(
        null=False,
        blank=False,
        max_length=15,
        choices=CHOICES
    )

    rating = models.FloatField(
        null=False,
        blank=False,
        validators=[
            rating_validator
        ]
    )

    max_level = models.IntegerField(
        null=True,
        blank=True,
        validators=[
            validators.MinValueValidator(1),
        ]
    )

    image_url = models.URLField(
        null=False,
        blank=False,
    )

    summary = models.TextField(
        null=True,
        blank=True
    )
