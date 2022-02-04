from dataclasses import field
from django import forms
from . import models
from .models import Contact
from django.forms.widgets import SelectMultiple, TextInput, Textarea, EmailInput, CheckboxInput,URLInput, Select, NumberInput, RadioSelect, FileInput


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields= '__all__'
        widgets={
            'name':TextInput(attrs={'class':'required form-control','placeholder':"Name"}),
            'company':TextInput(attrs={'class':'required form-control','placeholder':"Company"}),
            'phone':TextInput(attrs={'class':'required form-control','placeholder':"Phone"}),
            'email':EmailInput(attrs={'class':'form-control','placeholder':"Email"}),
            'website':TextInput(attrs={'class':'form-control','placeholder':"Website"}),
            
            'ad_type':RadioSelect(attrs={'id':"html", 'name':"fav" ,'value':"Outdoor_Advertising"}),
            # 'ad_type':RadioSelect(attrs={'id':"css", 'name':"fav" ,'value':"Agency_Partnership"}),


        }