from django.db import models
from wagtail.images.edit_handlers import ImageChooserPanel
from wagtail.core.models import Page,Orderable
from modelcluster.fields import ParentalKey
from wagtail.core.fields import RichTextField
from wagtail.admin.edit_handlers import (
    FieldPanel,
    InlinePanel,
    MultiFieldPanel,
    StreamFieldPanel,
)

class HomePage(Page):
    image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+',
        help_text='Homepage image'
    )
    vision_title = models.CharField(
        null=True,
        blank=True,
        max_length=100,
        help_text='Vision'
    )
    vision_image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+',
        help_text='Vision image'
    )
    vision_text = RichTextField(
        null=True,
        blank=True,
        max_length=400,
        help_text='Write vision'
    )
    mission_title = RichTextField(
        null=True,
        blank=True,
        max_length=400,
        help_text='Mission title'
    )
    content_panels = Page.content_panels + [
        ImageChooserPanel(
            'image',heading="Home Page"),
        MultiFieldPanel([
            FieldPanel('vision_title', classname="full"),
            ImageChooserPanel('vision_image'),
            FieldPanel('vision_text', classname="full"),
        ], heading="Vision section"),
        MultiFieldPanel([
            FieldPanel('mission_title',classname="full"),
            InlinePanel('missions',label="Mission"),
        ], heading="Missions")
        
    ]
class Mission(Orderable):
    page = ParentalKey(HomePage, on_delete=models.CASCADE, related_name='missions')
    list_label = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+',
        help_text='List label'
    )
    mission = models.CharField(blank=True, max_length=250)
    panels= [
        ImageChooserPanel('list_label'),
        FieldPanel('mission')
    ]