from django import template

from ..models import Menu, Footer

register = template.Library()


@register.simple_tag()
def get_menu(slug):
    return Menu.objects.get(slug=slug)

@register.inclusion_tag('include/footer.html', takes_context=True)
def get_footer(context):
    footer = Footer.objects.first() 
    return {
        'footer':footer
    }