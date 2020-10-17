from django import template

register = template.Library()

@register.filter(name='cut_example')
def cut_example(value,arg):
    """
    This cuts out all values of "arg" from the string!
    """

    return value.replace(arg,'')

# register.filter('cut_example',cut_example)
