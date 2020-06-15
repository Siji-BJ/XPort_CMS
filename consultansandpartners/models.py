from django.db import models
from wagtail.core.models import Page,Orderable
from wagtail.images.edit_handlers import ImageChooserPanel
# Create your models here.
class ConsultansAndPartners(Page):
    header_image= models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=False,
        on_delete=models.SET_NULL,
        related_name='+',
        help_text='Image in header'
    )
    content_panels = Page.content_panels + [
        ImageChooserPanel('header_image', heading= 'Header Image')
    ]
