# Generated by Django 3.0.7 on 2020-06-30 06:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0026_delete_advert'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='homepage',
            name='from_address',
        ),
        migrations.RemoveField(
            model_name='homepage',
            name='subject',
        ),
        migrations.RemoveField(
            model_name='homepage',
            name='to_address',
        ),
    ]