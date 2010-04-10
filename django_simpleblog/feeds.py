from django.contrib.syndication.feeds import Feed
from django.utils.feedgenerator import Atom1Feed
from django.shortcuts import get_object_or_404
from django.conf import settings

from models import Entry

CATEGORIES = getattr(settings, 'CATEGORIES', True)
if CATEGORIES:
    from models import Category


FEED_DEFAULTS = {'latest': {'title': 'Simpleblog Latest 10 Entries',
                            'link':  '/news/',
                            'description': 'Simpleblog RSS Newsfeed',
                            'length': 10},}
if CATEGORIES:
    FEED_DEFAULTS['category'] = {'title': 'Simpleblog Categoryfeed %s',
                                 'link': ''
                                 'description': 'Feed For Category "%s"'}

FEED_SETTINGS = getattr(settings, 'FEED_SETTINGS', FEED_DEFAULTS)

class RSSLatestEntries(Feed):
    title = FEED_SETTINGS['latest']['title']
    link = FEED_SETTINGS['latest']['link']
    description = FEED_SETTINGS['latest']['description']

    def items(self):
        return Entry.objects.order_by('-created')[:FEED_SETTINGS['latest']['length']

    def item_pubdate(self, item):
        return item.created

class AtomLatestEntries(RSSLatestEntries):
    feed_type = Atom1Feed
    subtitle = RSSLatestEntries.description

if CATEGORIES:  
    class RSSCategoryFeed(Feed):
        def get_object(self, request, category_name):
            return get_object_or_404(Category, name=category_name)

        def title(self, item):
            return FEED_SETTINGS['category']['title'] % item.name

        def description(self, item):
            return FEED_SETTINGS['category']['description'] % item.name

        def items(self, item):
            return Entry.objects.filter(category=category_name).order_by('-created')
