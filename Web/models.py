from distutils.command.upload import upload
from turtle import title
from django.db import models
from versatileimagefield.fields import VersatileImageField,PPOIField
# Create your models here.

class Service(models.Model):
    title=models.CharField(max_length=225)
    description = models.TextField()
    image = VersatileImageField(
        'Image',
        upload_to='services/',
        ppoi_field='ppoi'
    )
    ppoi = PPOIField(
        'Image PPOI'
    )

    subtitle=models.CharField(max_length=225)
    subdescription = models.TextField()
    


    def __str__(self):
        return self.title

    
class Term(models.Model):
    service=models.ForeignKey(Service,on_delete=models.CASCADE)
    term=models.CharField(max_length=225)

class Gallery(models.Model):
    title=models.CharField(max_length=225)
    image = VersatileImageField(
        'Image',
        upload_to='gallery/',
        ppoi_field='ppoi'
    )
    ppoi = PPOIField(
        'Image PPOI'
    )


     