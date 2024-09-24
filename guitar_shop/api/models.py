from django.db import models

class Guitars(models.Model):
    product_id = models.CharField(max_length=1000, blank=True)
    name = models.CharField(max_length=1000, blank=True)
    img = models.CharField(max_length=1000, blank=True)
    price = models.CharField(max_length=100, blank=True)


class Video(models.Model):
    file = models.FileField(upload_to='videos/')