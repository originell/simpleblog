from django.db import models
from django.utils.translation import ugettext_lazy as _
from utils import make_rst

class Entry(models.Model):
    ''' A single (simple) blog entry '''

    created = models.DateTimeField(editable=False)
    modified = models.DateTimeField(editable=False)

    title = models.CharField(_('Titel'), max_length=79)
    slug = models.SlugField(unique_for_date='created')
    body = models.TextField(_('Eintrag'))
    body_html = models.TextField(editable=False)

    class Meta:
        verbose_name = _('Entry')
        verbose_name_plural = _('Entries')

    def __unicode__(self):
        return self.title

    def save(self):
        self.body_html = make_rst(self.body)
        super(Entry, self).save()
