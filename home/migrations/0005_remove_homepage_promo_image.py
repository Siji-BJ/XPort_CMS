# Generated by Django 3.0.7 on 2020-06-11 16:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_auto_20200611_2200'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='homepage',
            name='promo_image',
        ),
    ]
