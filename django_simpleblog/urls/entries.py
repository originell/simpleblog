from django.conf.urls.defaults import *
from django_simpleblog.models import Entry

entry_info_dict = {'queryset': Entry.objects.all(),
                   'date_field': 'created',}

urlpatterns = patterns('django.views.generic.date_based',
    (r'^$', 'archive_index', entry_info_dict, 'blog_archive_index'),
    (r'^(?P<year>\d{4})/$', 'archive_year', entry_info_dict,
        'blog_archive_year'),
    (r'^(?P<year>\d{4})/(?P<month>\w{3})/$', 'archive_month',
        entry_info_dict, 'blog_archive_month'),
    #(r'^(?P<year>\d{4})/(?P<month>\w{3})/(?P<day>\w{2})/$', 'archive_day',
    #    entry_info_dict, 'blog_archive_day'),
    (r'^(?P<year>\d{4})/(?P<month>\w{3})/(?P<day>\w{2})/(?P<slug>[-\w]+)/$',
        'object_detail', entry_info_dict, 'blog_entry_detail'),
)
