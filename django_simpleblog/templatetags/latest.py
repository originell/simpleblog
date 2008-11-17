from django import template
from django_simpleblog.models import Entry

register = template.Library()

class EntryNode(template.Node):
    def __init__(self, varname):
        self.varname = varname

    def __repr__(self):
        return "<Entry Node>"

    def render(self, context):
        context[self.varname] = Entry.objects.latest()
        return ''

class GetLatestEntry:
    """
    Returns 10 newest Objekte.

    Usage::

        {% latest_entry as entry %}
    """
    def __init__(self, tag_name):
        self.tag_name = tag_name

    def __call__(self, parser, token):
        tokens = token.contents.split()
        if len(tokens) < 3:
            raise template.TemplateSyntaxError, \
                "'%s' statements require two arguments" % self.tag_name
        if tokens[1] != 'as':
            raise template.TemplateSyntaxError, \
                "Second argument in '%s' must be 'as'" % self.tag_name
        return EntryNode(varname=tokens[2])

register.tag('latest_entry', GetLatestEntry('latest_entry'))
