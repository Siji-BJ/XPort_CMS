from django.db import models
from wagtail.core.models import Page
from wagtail.images.edit_handlers import ImageChooserPanel
from wagtail.admin.edit_handlers import FieldPanel,MultiFieldPanel, InlinePanel
from wagtail.core.fields import RichTextField
from modelcluster.fields import ParentalKey

class AboutUsPage(Page):
    image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+',
        help_text = 'Landscape mode only; Approximate dimension: 1440 px (width) x 360 px (height)'
    )
    history_title = models.CharField(
        null=True,
        blank=True,
        max_length=255,
    )
    main_text = RichTextField(
        null=True,
        blank=True,
    )
    side_text = models.TextField(
        null=True,
        blank=True,
    )
    history_image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+',
        help_text = 'Approximate dimension: 440 px (width) x 540 px (height)'
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
    body_side_text = models.TextField(
        null=True,
        blank=True,
    )
    body_text_2 = RichTextField(
        null=True,
        blank=True,
    )
    body_text_3 = RichTextField(
        null=True,
        blank=True,
    )
    body_text_4 = RichTextField(
        null=True,
        blank=True,
    )
    team_title = models.CharField(
        null=True,
        blank=True,
        max_length=255,
    )
    
    
    content_panels = Page.content_panels + [   
            MultiFieldPanel([
                ImageChooserPanel('image'),
            ], heading = "Banner section"),
            MultiFieldPanel([              
                FieldPanel('history_title'),
                FieldPanel('main_text'),
                FieldPanel('side_text'),
                ImageChooserPanel('history_image')
            ], heading="History Section"),
            MultiFieldPanel([              
                FieldPanel('body_title'),
                FieldPanel('body_text_1'),
                FieldPanel('body_text_2'),
                InlinePanel('points', label="Points"), 
                FieldPanel('body_text_3'),
                FieldPanel('body_side_text'),
                InlinePanel('photo', label = "Images"),
                FieldPanel('body_text_4'),
            ], heading="Body Section"),
            FieldPanel('team_title'),
            InlinePanel('team', label = "Team"),

          
    ]

class Points(models.Model):
    page = ParentalKey(AboutUsPage, on_delete=models.CASCADE, related_name='points')
    point = models.TextField(
        null=True,
        blank=True,
    )
    panels = [
        FieldPanel('point'),
    ]

class Photo(models.Model):
    page = ParentalKey(AboutUsPage, on_delete=models.CASCADE, related_name='photo')
    gallery_image = models.ForeignKey(
        'wagtailimages.Image', null=True, blank=True,
        on_delete=models.SET_NULL, related_name='+',
        help_text = 'Approximate dimension: 95 px (width) x 90 px (height)'
        
    )
    caption = models.TextField(
        null=True,
        blank=True,
    )
    panels = [
        ImageChooserPanel('gallery_image'),
        FieldPanel('caption'),
    ]

class Team(models.Model):
    page = ParentalKey(AboutUsPage, on_delete=models.CASCADE, related_name='team')
    photo = models.ForeignKey(
        'wagtailimages.Image', null=True, blank=True,
        on_delete=models.SET_NULL, related_name='+',
        help_text = 'Approximate dimension: 300 px (width) x 300 px (height)'
    )
    name = models.TextField(
        null=True,
        blank=True,
    )
    designation = models.TextField(
        null=True,
        blank=True,
    )
    profile = RichTextField(
        null=True,
        blank=True,
    )
    panels = [
        ImageChooserPanel('photo'),
        FieldPanel('name'),
        FieldPanel('designation'),
        FieldPanel('profile'),
    ]


# Create your models here.
