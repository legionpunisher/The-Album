from django.db import models

# Create your models here.
class Image(models.Model):
    image = models.ImageField()
    image_name = models.CharField(max_length=30)
    Description = models.CharField(max_length=30)
    