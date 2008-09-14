from django.db import models
from django.utils.translation import ugettext_lazy as _
from utils.make_rst import make_rst
from django.conf import settings

TAGGING = getattr(settings, 'TAGGING', True)
CATEGORIES = getattr(settings, 'CATEGORIES', True)

if TAGGING:
    # thx to django-photologue
    try:
        from tagging.fields import TagField
        TAGFIELD_HELP = _('Separate tags with spaces, '\
                          'put quotes around multiple-word tags.')
    except ImportError:
        class TagField(models.CharField):
            def __init__(self, **kwargs):
                default_kwargs = {'max_length': 255, 'blank': True}
                default_kwargs.update(kwargs)
                super(TagField, self).__init__(**default_kwargs)
            def get_internal_type(self):
                return 'CharField'
        TAGFIELD_HELP = _('Django-tagging was not found, ' \
                          'tags will be treated as plain text.')

if CATEGORIES:
    class Category(models.Model):
        ''' A category '''

        name = models.CharField(_('name'), max_length=30)

        class Meta:
            verbose_name = _('Category')
            verbose_name_plural = _('Categories')
            ordering = ['name',]

        def __unicode__(self):
            return self.name

class Entry(models.Model):
    ''' A single (simple) blog entry '''

    created = models.DateTimeField(editable=False)
    modified = models.DateTimeField(editable=False)

    title = models.CharField(_('title'), max_length=79)
    slug = models.SlugField(unique_for_date='created')
    body = models.TextField(_('post'))
    body_html = models.TextField(editable=False)

    if CATEGORIES:
        category = models.ForeignKey(Category)
    if TAGGING:
        tags = TagField(help_text=TAGFIELD_HELP, verbose_name=_('tags'))

    class Meta:
        verbose_name = _('Entry')
        verbose_name_plural = _('Entries')
        get_latest_by = 'created'
        ordering = ['-created', 'title']

    def __unicode__(self):
        return self.title

    def save(self):
        self.body_html = make_rst(self.body)
        super(Entry, self).save()

    def get_absolute_url(self):
        return ('blog_entry_detail', (),
                                    {'year': self.created.strftime('%Y'),
                                     'month': self.created.strftime('%b'). \
                                              lower(),
                                     'day': self.created.strftime('%d'),
                                     'slug': self.slug },)
    get_absolute_url = models.permalink(get_absolute_url)
