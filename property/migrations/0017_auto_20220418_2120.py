# Generated by Django 2.2.24 on 2022-04-18 18:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0016_auto_20220415_2207'),
    ]

    operations = [
        migrations.AlterField(
            model_name='flat',
            name='new_building',
            field=models.NullBooleanField(db_index=True, verbose_name='Здание, построенное после 2015г.'),
        ),
    ]
