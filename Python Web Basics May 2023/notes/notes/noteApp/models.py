from django.db import models


# Create your models here.

class ProfileModel(models.Model):
    first_name = models.CharField(max_length=20, verbose_name="First Name")
    last_name = models.CharField(max_length=20, verbose_name="Last Name")
    age = models.IntegerField()
    image_url = models.URLField(verbose_name="Link to Profile Image")


class NoteModel(models.Model):
    title = models.CharField(max_length=30)
    content = models.TextField()
    image_url = models.URLField(verbose_name='Link to Image')
