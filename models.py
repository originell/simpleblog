from django.db import models
from django.utils.translation import ugettext_lazy as _
from utils.make_rst import make_rst

class Entry(models.Model):
    ''' A single (simple) blog entry '''

    created = models.DateTimeField(editable=False)
    modified = models.DateTimeField(editable=False)

    title = models.CharField(_('Title'), max_length=79)
    slug = models.SlugField(unique_for_date='created')
    body = models.TextField(_('Post'))
    body_html = models.TextField(editable=False)

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
        return ('entry_detail', (), {'year': self.created.strftime('%Y'),
                                     'month': self.created.strftime('%b'). \
                                              lower(),
                                     'day': self.created.strftime('%d'),
                                     'slug': self.slug })
    get_absolute_url = models.permalink(get_absolute_url)
