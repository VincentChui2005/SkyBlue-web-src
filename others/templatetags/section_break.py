from django import template


register = template.Library()

@register.simple_tag()
def section_breaker():
    return '<div class="section-break" style="padding-top: 1.5rem; padding-bottom: 1.5rem"><div class="breaker"></div></div>'
