from django.conf.urls.defaults import *
from django_simpleblog.feeds import RSSLatestEntries, AtomLatestEntries

feeds = {
    'rss': RSSLatestEntries,
    'atom': AtomLatestEntries,
}

urlpatterns = patterns('',
    (r'^feeds/(?P<url>.*)/$', 'django.contrib.syndication.views.feed',
        {'feed_dict': feeds}),
)
