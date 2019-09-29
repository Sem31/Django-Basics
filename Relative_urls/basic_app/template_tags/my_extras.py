from django import template

register = template.Library()

@register.filter(name='cut') #decorater way
def cut(value,arg):
    """
    this cuts out the values of "args" from the string
    """
    return value.replace(arg,'')

# register.filter('cut',cut) custom way