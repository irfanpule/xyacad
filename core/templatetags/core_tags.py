from django.template import Library

register = Library()


@register.filter(name='addclass')
def addclass(field, class_attr):
    return field.as_widget(attrs={'class': class_attr})


@register.filter(name='get_column_bootstrap')
def get_column_bootstrap(number):
    if number >= 0 and number <= 4:
        column = 12 / number
        return f"col-md-{int(column)}"
    return "col-md-3"
