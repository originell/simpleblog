from django.conf.urls.defaults import *
from django.conf import settings
from django_simpleblog.feeds import *

CATEGORIES = getattr(settings, 'CATEGORIES', True)
if CATEGORIES:
    urlpatterns = patterns('',
        (r'^category/(?P<category_name>\w+)/rss/$', RSSCategoryFeed()),
        (r'^category/(?P<category_name>\w+)/atom/$', AtomCategoryFeed()),
    )


default_pattern = patterns('',
        (r'^latest/rss/$', RSSLatestEntries),
        (r'^latest/atom/$', AtomLatestEntries),
)

try:
    urlpatterns += default_pattern
except NameError:
    urlpatterns = default_pattern
