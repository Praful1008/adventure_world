from django.db import models

# Create your models here.

class Destination(models.Model) :

    place = models.CharField(max_length=100)
    price = models.IntegerField(default = 0)
    about = models.TextField()
    image_url = models.ImageField(upload_to='img')

