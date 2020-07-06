from django.db import models
from wagtail.images.edit_handlers import ImageChooserPanel
from wagtail.core.models import Page,Orderable
from modelcluster.fields import ParentalKey
from wagtail.core.fields import RichTextField, StreamField
from wagtail.admin.edit_handlers import (
    FieldPanel,
    InlinePanel,
    MultiFieldPanel,
    StreamFieldPanel,
    FieldRowPanel,
)
from wagtail.contrib.forms.models import AbstractEmailForm, AbstractFormField

class HomePage(AbstractEmailForm):
    image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=False,
        on_delete=models.SET_NULL,
        related_name='+',
        help_text='Landscape mode only; Approximate dimension: 1440 px (width) x 640 px (height)'
    )

    vision_title = models.CharField(
        null=True,
        blank=False,
        default='Vision',
        max_length=100,
        help_text='Title section'
    )
    vision_image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=False,
        on_delete=models.SET_NULL,
        related_name='+',
        help_text='PNG file with approximate dimension 137 px (width) x 137 px (height)'
    )
    vision_text = RichTextField(
        null=True,
        blank=False,
        default=' ',
        max_length=400,
        help_text='Text to display Vision'
    )
    mission_title = models.CharField(
        blank=False,
        default='Mission',
        max_length=250,
        help_text='Title section'
    )
    mission_list_label = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=False,
        on_delete=models.SET_NULL,
        related_name='+',
        help_text='PNG file with approximate dimension 17 px (width) x 13 px (height)'
    )
    objectives_title = models.CharField(
        blank=False,
        default='Objectives',
        max_length=250,
        help_text='Objective title'
        )
    objectives_background_image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=False,
        on_delete=models.SET_NULL,
        related_name='+',
        help_text='PNG file with approximate dimension 1440 px (width) x 800 px (height)'
    )
    objectives_side_image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=False,
        on_delete=models.SET_NULL,
        related_name='+',
        help_text='PNG file with approximate dimension 670 px (width) x 560 px (height)'
    )
    usp_title = models.CharField(
        blank=False,
        default='Our USP',
        max_length=250,
        help_text='Title section'
    )
    usp_side_image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=False,
        on_delete=models.SET_NULL,
        related_name='+',
        help_text='PNG file with approximate dimension 410 px (width) x 570 px (height)'
    )
    contact_us_button_text = models.CharField(
        blank=True,
        default=' ',
        max_length=250,
        help_text='Text displayed inside the contact us button'
        )
    image_inside_contact_us_button = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+',
        help_text='Arrow displayed inside the contact us button.'
    )
    primary_support_item_image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+',
        help_text='Image diplayed on the left side of support section. Use PNG file with approximate dimension 360 px (width) x 580 px (height) '
    )
    support_title = models.CharField(
        blank=False,
        default='24X7 Support',
        max_length=250
    )
    support_text = models.CharField(
        blank=False,
        default=' ',
        max_length=500
    )
    background_image_of_support = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+',
        help_text='Background image of support text. Use PNG file with approximate dimension 360 px (width) x 580 px (height)'
    )
    download_image_for_brochure = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=False,
        on_delete=models.SET_NULL,
        related_name='+',
        help_text='Download icon for brochure. Use PNG file with approximate dimension 26 px (width) x 26 px (height) '
    )
    download_text_with_brochure = models.CharField(
        blank=True,
        default='Click here to download',
        max_length=250
    )
    contact_us_title = models.CharField(
        blank=False,
        default='CONTACT US',
        max_length=250
    )
    intro =  models.CharField(blank=True,max_length=250)
    content_panels = AbstractEmailForm.content_panels + [
        MultiFieldPanel([
            ImageChooserPanel('image',heading="Home Page"),
            ], heading = "Main home page"),       
        MultiFieldPanel([
            FieldPanel('vision_title', classname="full"),
            ImageChooserPanel('vision_image'),
            FieldPanel('vision_text', classname="full"),
        ], heading="Vision section"),
        MultiFieldPanel([
            FieldPanel('mission_title',classname="full"),
            ImageChooserPanel('mission_list_label',classname='full'),
            InlinePanel('missions',label="Mission"),
        ], heading="Missions"),
        MultiFieldPanel([
            FieldPanel('objectives_title',classname="full"),
            ImageChooserPanel('objectives_background_image',classname="full"),
            ImageChooserPanel('objectives_side_image',classname="full"),
            InlinePanel('objectives',label="Objective"),
        ], heading="Objectives"),
        MultiFieldPanel([
            FieldPanel('usp_title',classname='full'),
            ImageChooserPanel('usp_side_image',classname='full'),
            FieldPanel('contact_us_button_text',classname='full'),
            ImageChooserPanel('image_inside_contact_us_button',classname='full'),
            InlinePanel('usps',label="USP")
        ],heading="Our USP"),
        MultiFieldPanel([
            ImageChooserPanel('primary_support_item_image',classname='full'),
            ImageChooserPanel('download_image_for_brochure',classname='full'),
            FieldPanel('download_text_with_brochure',classname='full'),
            InlinePanel('brochure_list',label = 'Brochure'),
            ImageChooserPanel('background_image_of_support',classname='full'),
            FieldPanel('support_title',classname='full'),
            FieldPanel('support_text',classname='full'),
        ], heading="Support Details"),
        MultiFieldPanel([
            FieldPanel('contact_us_title'),
            FieldPanel('intro'),
            InlinePanel('form_fields', label="Form fields"),
        ],"Contact Us")    
    ]


class Mission(Orderable):
    page = ParentalKey(HomePage, on_delete=models.CASCADE, related_name='missions')
    mission = models.CharField(
        blank=False,
        default=' ',
        max_length=250
    )
    panels= [
        FieldPanel('mission')
    ]


class Objective(Orderable):
    page = ParentalKey(HomePage, on_delete=models.CASCADE, related_name='objectives')
    objective_text = models.CharField(
        blank=False,
        default=' ',
        max_length=250
    )
    objective_image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=False,
        on_delete=models.SET_NULL,
        related_name='+',
        help_text='PNG file with approximate dimension 52 px (width) x 54 px (height)'
    )
    panels = [
        FieldPanel('objective_text'),
        ImageChooserPanel('objective_image')
    ]

class USP(Orderable):
    page = ParentalKey(HomePage, on_delete=models.CASCADE, related_name='usps')
    usp= models.CharField(
        blank=False,
        default=' ',
        max_length=250
    )
    panels = [
        FieldPanel('usp')
    ]

class Brochure(Orderable):
    page = ParentalKey(HomePage, on_delete=models.CASCADE, related_name='brochure_list')
    brochure_name = models.CharField(
        blank=False,
        default=' ',
        max_length=400
    ) 
    panels = [
        FieldPanel('brochure_name')
    ]   

class FormField(AbstractFormField):
    page = ParentalKey('HomePage', related_name='form_fields', on_delete=models.CASCADE)
