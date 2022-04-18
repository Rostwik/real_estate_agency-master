# Generated by Django 2.2.24 on 2022-03-18 17:16
from django.db import migrations


def fill_owner_pure_phone(apps, schema_editor):
    Flat = apps.get_model('property', 'Flat')
    Owner = apps.get_model('property', 'Owner')

    for flat in Flat.objects.all().iterator():
        Owner.objects.get_or_create(
            owner=flat.owner,
            owners_phonenumber=flat.owners_phonenumber,
            owner_pure_phone=flat.owner_pure_phone
        )


class Migration(migrations.Migration):
    dependencies = [
        ('property', '0010_auto_20220318_1339'),
    ]

    operations = [
        migrations.RunPython(fill_owner_pure_phone)
    ]
