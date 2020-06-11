from django.db import models
from wagtail.images.edit_handlers import ImageChooserPanel
from wagtail.core.models import Page


class HomePage(Page):
    image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+',
        help_text='Homepage image'
    )
    content_panels = Page.content_panels + [
        ImageChooserPanel('image')
    ]