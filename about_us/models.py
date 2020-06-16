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
            ImageChooserPanel('image'),
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
                FieldPanel('body_text_3'),
                FieldPanel('body_side_text'),
                InlinePanel('points', label="Points"), 
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
        on_delete=models.SET_NULL, related_name='+'
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
        on_delete=models.SET_NULL, related_name='+'
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
