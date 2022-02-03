from dataclasses import field
from django import forms
from . import models
from .models import Contact
from django.forms.widgets import SelectMultiple, TextInput, Textarea, EmailInput, CheckboxInput,URLInput, Select, NumberInput, RadioSelect, FileInput


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        field= '__all__'
        widgets={
            'name':TextInput(attrs={'class':'required form-control','placeholder':"Name"}),
            'company':TextInput(attrs={'class':'required form-control','placeholder':"Company"}),
            'phone':TextInput(attrs={'class':'required form-control','placeholder':"Phone"}),
            'email':EmailInput(attrs={'class':'form-control','placeholder':"Email"}),
            'wesite':TextInput(attrs={'class':'form-control','placeholder':"Website"}),
            'ad_type':RadioSelect(attrs={'class':'form-control','placeholder':"Website"})

        }