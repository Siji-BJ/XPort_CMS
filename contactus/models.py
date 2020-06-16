from django.db import models
from wagtail.core.models import Page,Orderable
from wagtail.images.edit_handlers import ImageChooserPanel
from wagtail.core.fields import RichTextField
from modelcluster.fields import ParentalKey
from wagtail.admin.edit_handlers import (
    FieldPanel,
    InlinePanel,
    MultiFieldPanel,

)

class ContactUsPage(Page):
    header_image= models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=False,
        on_delete=models.SET_NULL,
        related_name='+',
        help_text='Image in header'
    )
    content_panels = Page.content_panels + [
        ImageChooserPanel('header_image', heading= 'Header Image'),
        MultiFieldPanel([
            InlinePanel('contents',label='Details')
        ], heading= 'Details'),
        MultiFieldPanel([
            InlinePanel('contact_details',label='Details')
        ], heading= 'Contact Details'),
    ]
class Contents(Orderable):
    page = ParentalKey('ContactUsPage', on_delete=models.CASCADE, related_name='contents')
    content_title = models.CharField(
        blank=False,
        default=' ',
        max_length=250
    )   
    content_body = RichTextField(
        null=True,
        blank=False,
        default=' ',
        max_length=1400,
        help_text='Body'
    )
    panels = [
        FieldPanel('content_title',classname='full'),
        FieldPanel('content_body', classname='full')
    ]

class ContactDeatils(Orderable):
    page = ParentalKey('ContactUsPage', on_delete=models.CASCADE, related_name= 'contact_details')
    name = models.CharField(
        blank=False,
        default=' ',
        max_length=250
    )   
    email_address = models.CharField(
        blank=False,
        default=' ',
        max_length=250
    )  
    panels = [
        FieldPanel('name',classname='full'),
        FieldPanel('email_address', classname='full')
    ]