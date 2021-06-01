from django.db import models

# Create your models here.
class Image(models.Model):
 photo = models.ImageField(upload_to="myimage")
 date = models.DateTimeField(auto_now_add=True)
class Clusters(models.Model):
 cluster = models.CharField(max_length=500,primary_key=True)
 frequency = models.CharField(max_length=250)
 image_hash = models.CharField(max_length=500)
 status = models.CharField(max_length=500)
 updated_image = models.ImageField(upload_to="myimage")
 lat = models.CharField(max_length=500)
 lon = models.CharField(max_length=500)