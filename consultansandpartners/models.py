from django.db import models
from wagtail.core.models import Page,Orderable
from wagtail.images.edit_handlers import ImageChooserPanel
from wagtail.core.fields import RichTextField
from wagtail.admin.edit_handlers import (
    FieldPanel,
    InlinePanel,
    MultiFieldPanel
    )
from modelcluster.fields import ParentalKey

class ConsultansAndPartners(Page):
    header_image= models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=False,
        on_delete=models.SET_NULL,
        related_name='+',
        help_text = 'Landscape mode only; Approximate dimensions: 1440 px (width) x 360 px (height)'
    )
    consultans_Partners_image = models.ForeignKey(
        'wagtailimages.Image',
        null = True,
        blank = True,
        on_delete= models.SET_NULL,
        related_name= '+',
        help_text = 'Approximate dimension: 465 px (width) x 425 px (height)'
    )
    consultans_Partners_body = RichTextField(
        null=True,
        blank=False,
        default=' ',
        max_length=1400,
        help_text='Body'
    )
    idp_program_title=models.CharField(
        blank=False,
        default='IDP Program',
        max_length=200
    )
    idp_program_body = RichTextField(
        null=True,
        blank=False,
        default=' ',
        max_length=1400,
        help_text='Body'
    )
    idp_program_image = models.ForeignKey(
        'wagtailimages.Image',
        null = True,
        blank = True,
        on_delete= models.SET_NULL,
        related_name= '+',
        help_text = 'Approximate dimension: 400 px (width) x 500 px (height)'
    )
    content_panels = Page.content_panels + [
        MultiFieldPanel([
                ImageChooserPanel('header_image'),
        ], heading = "Banner section"),
        MultiFieldPanel([ImageChooserPanel('consultans_Partners_image'),
        FieldPanel('consultans_Partners_body',classname='full'), 
        ], heading = "Intro" ),     
        MultiFieldPanel([ 
            FieldPanel('idp_program_title',classname='full'),  
            FieldPanel('idp_program_body',classname='full'),
            ImageChooserPanel('idp_program_image',classname='full'),
            
        ], heading= 'IDP Program Details')
       
    ] 
    

