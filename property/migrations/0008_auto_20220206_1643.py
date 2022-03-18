# Generated by Django 2.2.24 on 2022-02-06 13:43
import phonenumbers
from django.db import migrations


def fill_owner_pure_phone(apps, schema_editor):
    Flat = apps.get_model('property', 'Flat')
    for building in Flat.objects.all():
        building.owner_pure_phone = phonenumbers.parse(building.owners_phonenumber, 'RU')
        building.save()


def move_backward(apps, schema_editor):
    Flat = apps.get_model('property', 'Flat')
    for building in Flat.objects.all():
        building.owner_pure_phone = None
        building.save()

class Migration(migrations.Migration):
    dependencies = [
        ('property', '0007_flat_owner_pure_phone'),
    ]

    operations = [
        migrations.RunPython(fill_owner_pure_phone, move_backward)
    ]