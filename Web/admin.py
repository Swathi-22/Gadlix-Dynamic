from django.contrib import admin
from .models import  Service,Term
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