from django.conf.urls.defaults import *
from django_simpleblog.models import Entry
from django.conf import settings

COMMENTS = getattr(settings, 'COMMENTS', True)

entry_info_dict = {'queryset': Entry.objects.all(),
                   'date_field': 'created',}
entry_info_dict_month = entry_info_dict.copy()
entry_info_dict_month['month_format'] = '%m'

urlpatterns = patterns('django.views.generic.date_based',
    (r'^$', 'archive_index', entry_info_dict, 'blog_archive_index'),
    (r'^(?P<year>\d{4})/$', 'archive_year', entry_info_dict,
        'blog_archive_year'),
    (r'^(?P<year>\d{4})/(?P<month>\d{2})/$', 'archive_month',
        entry_info_dict_month, 'blog_archive_month'),
    #(r'^(?P<year>\d{4})/(?P<month>\w{3})/(?P<day>\w{2})/$', 'archive_day',
    #    entry_info_dict, 'blog_archive_day'),
    (r'^(?P<year>\d{4})/(?P<month>\d{2})/(?P<day>\w{2})/(?P<slug>[-\w]+)/$',
        'object_detail', entry_info_dict_month, 'blog_entry_detail'),
)

if COMMENTS:
    urlpatterns += patterns('',
        (r'^comments/', include('django.contrib.comments.urls')),)
