from django import template

from ..models import Menu, Footer

register = template.Library()


@register.simple_tag()
def get_menu(slug):
    return Menu.objects.get(slug=slug)

@register.inclusion_tag('include\footer.html')
def get_footer(Context):
    enquiry = Footer.objects.first  
    return {
        'enquiry':enquiry
    }