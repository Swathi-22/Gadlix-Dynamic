from django.urls import path

from . import views

app_name='Web'

urlpatterns = [
    path('', views.index,name='index'),
    path('about/', views.about,name='about'),
    path('services/', views.services,name='services'),
    path('service-details/<int:id>/', views.serviceDetails,name='serviceDetails'),
    path('gallery/', views.gallery,name='gallery'),
    path('updates/', views.blog,name='blog'),
    path('update-details/', views.blogDetails,name='blogDetails'),
    path('contact/', views.contact,name='contact'),


]
