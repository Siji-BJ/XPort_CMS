# Generated by Django 3.0.7 on 2020-06-18 12:55

from django.db import migrations, models
import django.db.models.deletion
import modelcluster.fields


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailimages', '0022_uploadedimage'),
        ('industry_directions', '0006_auto_20200618_1803'),
    ]

    operations = [
        migrations.CreateModel(
            name='GrowthChart',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('growth_year', models.TextField(blank=True, max_length=255, null=True)),
                ('name', models.TextField(blank=True, max_length=255, null=True)),
                ('growth_unit', models.CharField(blank=True, max_length=255, null=True)),
                ('growth_image', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.Image')),
                ('page', modelcluster.fields.ParentalKey(on_delete=django.db.models.deletion.CASCADE, related_name='chart', to='industry_directions.IndustryDirectionsPage')),
            ],
        ),
    ]