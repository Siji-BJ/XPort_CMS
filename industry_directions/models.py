from django.db import models
from wagtail.core.models import Page
from wagtail.images.edit_handlers import ImageChooserPanel
from wagtail.admin.edit_handlers import FieldPanel,MultiFieldPanel, InlinePanel
from wagtail.core.fields import RichTextField
from modelcluster.fields import ParentalKey


class IndustryDirectionsPage(Page):
    image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+',
    )
    body_image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+',
    )
    body_title = models.CharField(
        null=True,
        blank=True,
        max_length=255,
    )
    body_text_1 = RichTextField(
        null=True,
        blank=True,
    )
    body_text_2 = RichTextField(
        null=True,
        blank=True,
    )
    card_image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+',
    )
    card_title = models.CharField(
        null=True,
        blank=True,
        max_length=255,
    )
    card_text = RichTextField(
        null=True,
        blank=True,
    )
    base_title = models.CharField(
        null=True,
        blank=True,
        max_length=255,
    )
    base_text = RichTextField(
        null=True,
        blank=True,
    )
    chart_background = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+',
    )
    chart_image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+',
    )
    chart_title = models.CharField(
        null=True,
        blank=True,
        max_length=255,
    )
    
    
    content_panels = Page.content_panels + [    
            ImageChooserPanel('image'),
            MultiFieldPanel([
                ImageChooserPanel('body_image'),
                FieldPanel('body_title'),
                FieldPanel('body_text_1'),
                FieldPanel('body_text_2'),
            ], heading = "Body section"),
            MultiFieldPanel([
                ImageChooserPanel('chart_background'),
                ImageChooserPanel('chart_image'),
                FieldPanel('chart_title'),
            ], heading = "Growth chart section"),
            InlinePanel('chart', label = "Field"),
            MultiFieldPanel([
                ImageChooserPanel('card_image'),
                FieldPanel('card_title'),
                FieldPanel('card_text'),
            ], heading = "Card section"),
            InlinePanel('point', label = "Point"),
            MultiFieldPanel([
                FieldPanel('base_title'),
                FieldPanel('base_text'),
            ], heading = "Base section"),
    ]

class Points(models.Model):
    page = ParentalKey(IndustryDirectionsPage, on_delete=models.CASCADE, related_name='point')
    point_image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+',
    )
    point_title = models.CharField(
        null=True,
        blank=True,
        max_length=255,
    )
   
    point_text = models.TextField(
        null=True,
        blank=True,
    )
    panels = [
        ImageChooserPanel('point_image'),
        FieldPanel('point_title'),
        FieldPanel('point_text'),
    ]

class GrowthChart(models.Model):
    page = ParentalKey(IndustryDirectionsPage, on_delete=models.CASCADE, related_name='chart')
    growth_year = models.TextField(
        null=True,
        blank=True,
        max_length=255,
    )
    name = models.TextField(
        null=True,
        blank=True,
        max_length=255,
    )
    growth_image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+',
    )
    growth_unit = models.CharField(
        null=True,
        blank=True,
        max_length=255,
    )

    panels = [
        FieldPanel('growth_year'),
        ImageChooserPanel('growth_image'),
        FieldPanel('name'),
        FieldPanel('growth_unit'),       
    ]




# Create your models here.
