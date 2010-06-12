from django.contrib.syndication.views import Feed
from django.utils.feedgenerator import Atom1Feed
from django.shortcuts import get_object_or_404
from django.template.defaultfilters import truncatewords_html
from django.conf import settings

from models import Entry
CATEGORIES = getattr(settings, 'CATEGORIES', True)
if CATEGORIES:
    from models import Category


FEED_DEFAULTS = {'latest': {'title': 'Simpleblog Latest 10 Entries',
                            'link':  '/latest/',
                            'description': 'Simpleblog Newsfeed',
                            'length': 10,
                            'item_descr_length': 48,}
                }
if CATEGORIES:
    FEED_DEFAULTS['category'] = {'title': 'Simpleblog Categoryfeed',
                                 'link': '/category/',
                                 'description': 'Feed For Category "%s"'}

FEED_SETTINGS = getattr(settings, 'FEED_SETTINGS', FEED_DEFAULTS)

class RSSLatestEntries(Feed):
    title = FEED_SETTINGS['latest']['title']
    link = FEED_SETTINGS['latest']['link']
    description = FEED_SETTINGS['latest']['description']

    def items(self):
        return Entry.objects.order_by('-created')[:FEED_SETTINGS['latest']['length']]

    def item_pubdate(self, item):
        return item.created

    def item_description(self, item):
        return truncatewords_html(item.body_html, FEED_SETTINGS['latest']['item_descr_length'])

class AtomLatestEntries(RSSLatestEntries):
    feed_type = Atom1Feed
    subtitle = RSSLatestEntries.description

if CATEGORIES:
    class RSSCategoryFeed(Feed):
        def get_object(self, request, category_name):
            return get_object_or_404(Category, name=category_name)

        def title(self, obj):
            try:
                return FEED_SETTINGS['category']['title'] % obj.name
            except TypeError:
                return FEED_SETTINGS['category']['title']

        def link(self, obj):
            return FEED_SETTINGS['category']['link']

        def description(self, obj):
            try:
                return FEED_SETTINGS['category']['description'] % obj.name
            except TypeError:
                return FEED_SETTINGS['category']['description']

        def items(self, obj):
            return Entry.objects.filter(category=obj).order_by('-created')

        def item_pubdate(self, item):
            return item.created

        def item_description(self, item):
            return truncatewords_html(item.body_html, FEED_SETTINGS['latest']['item_descr_length'])

    class AtomCategoryFeed(RSSCategoryFeed):
        feed_type = Atom1Feed

        def subtitle(self, obj):
            return super(AtomCategoryFeed, self).description(obj)
