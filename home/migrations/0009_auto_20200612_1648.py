# Generated by Django 3.0.7 on 2020-06-12 11:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0008_auto_20200612_1547'),
    ]

    operations = [
        migrations.AlterField(
            model_name='homepage',
            name='mission_title',
            field=models.CharField(blank=True, help_text='Mission title', max_length=250, null=True),
        ),
    ]
