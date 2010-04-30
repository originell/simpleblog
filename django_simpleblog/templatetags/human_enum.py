from django import template
from django.db.models.query import QuerySet

register = template.Library()

class EnumNode(template.Node):
    def __init__(self, queryset, urlify):
        self.queryset = queryset
        self.urlify = urlify

    def __repr__(self):
        return "<Human Enumeration Node>"

    def render(self, context):
        urlify = self.urlify
        queryset = self.queryset
        
        output = ''
        iter_len = queryset.count() - 2
        i = 0
        for item in queryset:
            if i < iter_len:
                if urlify:
                    output += '&ldquo;<a href="%s">%s</a>&rdquo;, ' % (item.get_absolute_url(),
                                                           item)
                else:
                    output += '&ldquo;%s&rdquo;, ' % item
            elif iter_len == i:
                if urlify:
                    output += '&ldquo;<a href="%s">%s</a>&rdquo; and ' % (item.get_absolute_url(),
                                                              item)
                else:
                    output += '&ldquo;%s&rdquo; and ' % item
            else:
                if urlify:
                    output += '&ldquo;<a href="%s">%s</a>&rdquo;' % (item.get_absolute_url(),
                                                         item)
                else:
                    output += '&ldquo;%s&rdquo;' % item
            i += 1
        return output

class HumanEnumeration(object):
    """
    Creates a humanized enumeration of a specified queryset.

    Usage::

        {% human_enum YourQueryset %}

    or if you want to have urls to the object

        {% human_enum YourQueryset urlify %}

    The __unicode__() method in your model should return some kind of title
    of your object.
    If you enable the option to build urls, your model needs a get_absolute_url()
    method.
    """
    def __init__(self, tag_name):
        self.tag_name = tag_name

    def __call__(self, parser, token):
        tokens = token.contents.split()
        if len(tokens) < 2:
            raise template.TemplateSyntaxError, \
                "'%s' statement requires at least one argument" % self.tag_name

        if type(tokens[1]) != QuerySet:
            raise template.TemplateSyntaxError, \
                "First argument in '%s' must be a QuerySet" % self.tag_name

        urlify = False
        if tokens[2] == 'urlify':
            urlify = True
        return EnumNode(queryset=tokens[1], urlify=urlify)

register.tag('human_enum', HumanEnumeration('human_enum'))
