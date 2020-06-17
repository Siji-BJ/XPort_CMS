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

class Management1(models.Model):
    page = ParentalKey(OperationsManagementPage, on_delete=models.CASCADE, related_name='management_field')
    title1 = models.TextField(
        null=True,
        blank=True,
    )
    pic1 = models.ForeignKey(
        'wagtailimages.Image', null=True, blank=True,
        on_delete=models.SET_NULL, related_name='+'
    )
    content1 = models.TextField(
        null=True,
        blank=True,
    )
    title2 = models.TextField(
        null=True,
        blank=True,
    )
    pic2 = models.ForeignKey(
        'wagtailimages.Image', null=True, blank=True,
        on_delete=models.SET_NULL, related_name='+'
    )
    content2 = models.TextField(
        null=True,
        blank=True,
    )
    panels = [
        FieldPanel('title1'),
        ImageChooserPanel('pic1'),
        FieldPanel('content1'),
        FieldPanel('title2'),
        ImageChooserPanel('pic2'),
        FieldPanel('content2'),
    ]


# Create your models here.
