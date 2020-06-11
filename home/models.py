from django.db import models
from wagtail.images.edit_handlers import ImageChooserPanel
from wagtail.core.models import Page
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
    promo_image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+',
        help_text='Promo image'
    )
    vision_title = models.CharField(
        null=True,
        blank=True,
        max_length=255,
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
        help_text='Write some promotional copy'
    )
    content_panels = Page.content_panels + [
        ImageChooserPanel([
            'image'],heading="Home Page"),
        MultiFieldPanel([
            FieldPanel('vision_title', classname="full"),
            ImageChooserPanel('image'),
            FieldPanel('vision_text', classname="full"),
        ], heading="Vision section")
    ]