from django.db import models
from wagtail.images.edit_handlers import ImageChooserPanel
from django_extensions.db.fields import AutoSlugField
from modelcluster.fields import ParentalKey
from modelcluster.models import ClusterableModel
from wagtail.admin.edit_handlers import (
    MultiFieldPanel,
    InlinePanel,
    FieldPanel,
    PageChooserPanel,
)
from wagtail.core.models import Orderable
from wagtail.snippets.models import register_snippet


class MenuItem(Orderable):

    link_title = models.CharField(
        blank=True,
        null=True,
        max_length=50
    )
    link_url = models.CharField(
        max_length=500,
        blank=True
    )
    link_page = models.ForeignKey(
        "wagtailcore.Page",
        null=True,
        blank=True,
        related_name="+",
        on_delete=models.CASCADE,
    )
    open_in_new_tab = models.BooleanField(default=False, blank=True)

    page = ParentalKey("Menu", related_name="menu_items")

    panels = [
        FieldPanel("link_title"),
        FieldPanel("link_url"),
        PageChooserPanel("link_page"),
        FieldPanel("open_in_new_tab"),
    ]

    @property
    def link(self):
        if self.link_page:
            return self.link_page.url
        elif self.link_url:
            return self.link_url
        return '#'

    @property
    def title(self):
        if self.link_page and not self.link_title:
            return self.link_page.title
        elif self.link_title:
            return self.link_title
        return 'Missing Title'


@register_snippet
class Menu(ClusterableModel):
    """The main menu clusterable model."""

    title = models.CharField(max_length=100)
    slug = AutoSlugField(populate_from="title", editable=True)
    logo =  models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=False,
        on_delete=models.SET_NULL,
        related_name='+'
    )
    # slug = models.SlugField()

    panels = [
        MultiFieldPanel([
            FieldPanel("title"),
            FieldPanel("slug"),
            ImageChooserPanel('logo'),
        ], heading="Menu"),
        InlinePanel("menu_items", label="Menu Item")
    ]

@register_snippet
class Footer(ClusterableModel):
    title = models.CharField(max_length=150)
    panels = [
        MultiFieldPanel([
            FieldPanel('title'),
            InlinePanel('enquiry')
        ], heading= 'Enquiry')
    ]

    def __str__(self):
        return self.title

class Enquiry(Orderable):
    page = ParentalKey('Footer', on_delete=models.CASCADE, related_name= 'enquiry')
    enquiry_about = models.CharField(max_length=150)
    enquiry_mail = models.CharField(max_length=150)

    panels = [
        FieldPanel('enquiry_about'),
        FieldPanel('enquiry_mail'),

    ]        