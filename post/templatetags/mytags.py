from django import template

register = template.Library()

@register.simple_tag
def umap():
    file = ["{% url 'morepost:dayend' %}",'a',]

    for a in file:
        return a