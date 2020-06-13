# Generated by Django 3.0.7 on 2020-06-13 05:04

from django.db import migrations, models
import django.db.models.deletion
import wagtail.core.fields


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailimages', '0022_uploadedimage'),
        ('home', '0015_auto_20200612_2023'),
    ]

    operations = [
        migrations.AlterField(
            model_name='homepage',
            name='image',
            field=models.ForeignKey(help_text='Homepage image', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.Image'),
        ),
        migrations.AlterField(
            model_name='homepage',
            name='vision_image',
            field=models.ForeignKey(help_text='Vision image', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.Image'),
        ),
        migrations.AlterField(
            model_name='homepage',
            name='vision_text',
            field=wagtail.core.fields.RichTextField(default=' ', help_text='Write vision', max_length=400, null=True),
        ),
        migrations.AlterField(
            model_name='homepage',
            name='vision_title',
            field=models.CharField(default='Vision', help_text='Vision', max_length=100, null=True),
        ),
    ]