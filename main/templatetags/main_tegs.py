from django import template
from main.models import *

register = template.Library()


@register.inclusion_tag('main/header.html')
def main_show_header():
    return {}

@register.inclusion_tag('main/footer.html')
def main_show_footer():
    return {}
