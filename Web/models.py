from distutils.command.upload import upload
from tabnanny import verbose
from turtle import title
from django.db import models
from versatileimagefield.fields import VersatileImageField,PPOIField
from tinymce.models import HTMLField


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
    image = VersatileImageField('Image',upload_to='gallery/',ppoi_field='ppoi' )
    ppoi = PPOIField('Image PPOI')

    class Meta:
        verbose_name_plural = ("Gallery")

    def __str__(self):
        return str(self.title)



class Update(models.Model):
    title=models.CharField(max_length=225)
    summary=models.CharField(max_length=500)
    image=VersatileImageField('Image',upload_to='updates/',ppoi_field='ppoi' )
    ppoi = PPOIField('Image PPOI')
    date=models.DateField()
    content=HTMLField(blank=True, null=True)

    def __str__(self):
        return str(self.title)



class Client(models.Model):
    title=models.CharField(max_length=225)
    image=VersatileImageField('Image',upload_to='clients/',ppoi_field='ppoi' )
    ppoi = PPOIField('Image PPOI')

    def __str__(self):
        return str(self.title)


class Testimonial(models.Model):
    decription=models.CharField(max_length=500)
    name=models.CharField(max_length=225)
    designation=models.CharField(max_length=225)
    image=VersatileImageField('Image',upload_to='testimonials/',ppoi_field='ppoi' )
    ppoi = PPOIField('Image PPOI')

    def __str__(self):
        return str(self.name)



class Contact(models.Model):
    AD_CHOICES=(('outdoor_advertising','outdoor_advertising'),('agent_partnership','agent_partnership',))
    name=models.CharField(max_length=225)
    company=models.CharField(max_length=225)
    phone=models.CharField(max_length=12)
    email=models.EmailField()
    website=models.CharField(max_length=225)
    ad_type=models.CharField(max_length=128,choices=AD_CHOICES)

    def __str__(self):
        return str(self.name)





     