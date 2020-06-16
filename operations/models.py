from django.db import models
from wagtail.images.edit_handlers import ImageChooserPanel
from wagtail.admin.edit_handlers import FieldPanel,MultiFieldPanel, InlinePanel
from wagtail.core.models import Page
from modelcluster.fields import ParentalKey
from wagtail.core.fields import RichTextField

class OperationsManagementPage(Page):
    operations_image = models.ForeignKey(
       'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+',
    )
    operations_title = models.TextField(
        null=True,
        blank=True,   
    )
    operations_text = RichTextField(
        null=True,
        blank=True,   
    )
    content_panels = Page.content_panels + [    
            MultiFieldPanel([
                ImageChooserPanel('operations_image'),
                FieldPanel('operations_text'),
                FieldPanel('operations_title'),
            ]),
            InlinePanel('management_field', label="Management field"),
    ]

class Management(models.Model):
    page = ParentalKey(OperationsManagementPage, on_delete=models.CASCADE, related_name='management_field')
    title = models.TextField(
        null=True,
        blank=True,
        help_text='Text'
    )
    pic = models.ForeignKey(
        'wagtailimages.Image', null=True, blank=True,
        on_delete=models.SET_NULL, related_name='+'
    )
    content = models.TextField(
        null=True,
        blank=True,
        help_text='Text'
    )
    panels = [
        FieldPanel('title'),
        ImageChooserPanel('pic'),
        FieldPanel('content'),
    ]
# Create your models here.
