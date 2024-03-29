# Generated by Django 2.2.24 on 2022-02-06 17:22
import phonenumbers
from django.db import migrations


def fill_owner_pure_phone(apps, schema_editor):
    Flat = apps.get_model('property', 'Flat')
    for building in Flat.objects.all().iterator():
        pure_phone = phonenumbers.parse(building.owners_phonenumber, 'RU')
        if phonenumbers.is_valid_number(pure_phone):
            building.owner_pure_phone = pure_phone
            building.save()


class Migration(migrations.Migration):
    dependencies = [
        ('property', '0008_auto_20220206_1643'),
    ]

    operations = [
        migrations.RunPython(fill_owner_pure_phone)
    ]
