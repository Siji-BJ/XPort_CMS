from django.db import models
from wagtail.core.models import Page
from wagtail.images.edit_handlers import ImageChooserPanel
from wagtail.admin.edit_handlers import FieldPanel,MultiFieldPanel, InlinePanel
from wagtail.core.fields import RichTextField

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
    
    
    content_panels = Page.content_panels + [    
            ImageChooserPanel('image'),
            MultiFieldPanel([              
                FieldPanel('history_title'),
                FieldPanel('main_text'),
                FieldPanel('side_text'),
                ImageChooserPanel('history_image')
            ], heading="History Section"),
          
    ]



# Create your models here.
