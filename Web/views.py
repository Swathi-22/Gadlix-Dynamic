from django.shortcuts import render
from django.http import HttpResponse
from .models import Service, Term
# Create your views here.


def index(request):
    context={

    }
    return render(request,'web/index.html',context)


def about(request):
    context={

    }
    return render(request,'web/about.html',context)


def services(request):
    services = Service.objects.all()
    context={
        "services":services,

    }
    return render(request,'web/services.html',context)


def serviceDetails(request,id):
    service=Service.objects.get(id=id)
    terms=Term.objects.filter(service=service)
    context={
        "service":service,
        "terms":terms
    }
    return render(request,'web/service-details.html',context)


def gallery(request):
    context={

    }
    return render(request,'web/gallery.html',context)


def blog(request):
    context={

    }
    return render(request,'web/blog.html',context)


def blogDetails(request):
    context={

    }
    return render(request,'web/blog-details.html',context)


def contact(request):
    context={

    }
    return render(request,'web/contact.html',context)