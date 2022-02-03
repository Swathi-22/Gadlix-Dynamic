from django.contrib import admin
from .models import  Service,Term,Gallery,Update,Client,Testimonial,Contact
# Register your models here.


class TermInline(admin.TabularInline):
    model = Term

class ServiceAdmin(admin.ModelAdmin):
    list_display = ( 'title', 'description',)
    inlines = [
        TermInline,
    ]


admin.site.register(Service,ServiceAdmin)

admin.site.register(Term)

@admin.register(Gallery)
class GalleryAdmin(admin.ModelAdmin):
    list_display = ( 'title', 'image',)


@admin.register(Update)
class UpdateAdmin(admin.ModelAdmin):
    list_display = ( 'title', 'summary',)

@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ( 'title', 'image',)

@admin.register(Testimonial)
class TestimonialAdmin(admin.ModelAdmin):
    list_display = ( 'name', 'decription',)

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ( 'name', 'company',)