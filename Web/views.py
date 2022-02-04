from turtle import update
from urllib import response
from django.shortcuts import get_object_or_404, render
from django.http import JsonResponse
from django.http import HttpResponse
from .models import Service, Term,Gallery, Testimonial, Update,Client,Testimonial
from .forms import ContactForm
# Create your views here.
import json

def index(request):
    services = Service.objects.all()[:3]
    gallery1 = Gallery.objects.all().order_by('-id')[0:1]
    gallery2 = Gallery.objects.all().order_by('-id')[1:2]
    gallery3 = Gallery.objects.all().order_by('-id')[2:3]
    gallery4 = Gallery.objects.all().order_by('-id')[3:4]
    
    testimonial = Testimonial.objects.all()
    updates = Update.objects.all()
    forms=ContactForm(request.POST or None)

    context={
        "is_index" : True,
        "services":services,
        "gallery1":gallery1,
        "gallery2":gallery2,
        "gallery3":gallery3,
        "gallery4":gallery4,
       
        "testimonial":testimonial,
        'updates':updates,
        'forms':forms
    

    }
    return render(request,'web/index.html',context)


def about(request):
    testimonial = Testimonial.objects.all()
    context={
        "is_about" : True,
        'testimonial':testimonial

    }
    return render(request,'web/about.html',context)


def services(request):
    services = Service.objects.all()
    testimonial = Testimonial.objects.all()
    client = Client.objects.all()
    context={
        "is_service" : True,
        "services":services,
        "testimonial":testimonial,
        "client":client,

    }
    return render(request,'web/services.html',context)


def serviceDetails(request,id):
    service=Service.objects.get(id=id)
    terms=Term.objects.filter(service=service)
    testimonial = Testimonial.objects.all()
    client = Client.objects.all()
    context={
        "service":service,
        "terms":terms,
        "testimonial":testimonial,
        "client":client,
    }
    return render(request,'web/service-details.html',context)


def gallery(request):
    gallery = Gallery.objects.all()
    context={
        "is_gallery" : True,
        "gallery":gallery

    }
    return render(request,'web/gallery.html',context)


def blog(request):
    updates=Update.objects.all()
    context={
        "is_updates" : True,
        "updates":updates,

    }
    return render(request,'web/blog.html',context)


def blogDetails(request,slug):
    update = get_object_or_404(Update,slug=slug)
    updates=Update.objects.exclude(pk=update.pk)[:3]
    context={
        'update':update,
        'updates':updates
    }
    return render(request,'web/blog-details.html',context)


def contact(request):
    context={

    }
    return render(request,'web/contact.html',context)

def ajax(request):
    forms=ContactForm(request.POST or None)
    if request.method=='POST':
        if forms.is_valid():
            forms.save()
            response_data = {
                "status":"true",
                "title":"Successfully Submitted",
                "message":"Messages successfully updated"
            }
        return JsonResponse({'title':response_data})