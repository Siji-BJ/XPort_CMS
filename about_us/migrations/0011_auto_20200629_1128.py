# Generated by Django 3.0.7 on 2020-06-29 05:58

from django.db import migrations
import wagtail.core.fields


class Migration(migrations.Migration):

    dependencies = [
        ('about_us', '0010_aboutuspage_team_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aboutuspage',
            name='body_side_text',
            field=wagtail.core.fields.RichTextField(blank=True, null=True),
        ),
    ]