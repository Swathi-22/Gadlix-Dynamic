# Generated by Django 4.0.2 on 2022-02-02 06:27

from django.db import migrations
import versatileimagefield.fields


class Migration(migrations.Migration):

    dependencies = [
        ('Web', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='service',
            name='ppoi',
            field=versatileimagefield.fields.PPOIField(default='0.5x0.5', editable=False, max_length=20, verbose_name='Image PPOI'),
        ),
        migrations.AlterField(
            model_name='service',
            name='image',
            field=versatileimagefield.fields.VersatileImageField(upload_to='services/', verbose_name='Image'),
        ),
    ]