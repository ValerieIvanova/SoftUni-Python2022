from django.db import models


# Create your models here.


class Profile(models.Model):
    first_name = models.CharField(max_length=30, verbose_name="First Name")
    last_name = models.CharField(max_length=30, verbose_name="Last Name")
    image_url = models.URLField(verbose_name="Image URL")
