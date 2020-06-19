from django import template

from ..models import Menu, Footer

register = template.Library()


@register.simple_tag()
def get_menu(slug):
    return Menu.objects.get(slug=slug)

@register.inclusion_tag('templates/include/footer_text.html', takes_context=True)
def get_footers(context):
    return Footer.objects
