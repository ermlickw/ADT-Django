from django import template
register = template.Library()

from ..models import Claim

@register.inclusion_tag('children.html')
def custom_function(independent_claim):
    childs = independent_claim.childs.all()
    return {'childs': childs}
