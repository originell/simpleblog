from django.contrib.syndication.feeds import Feed
from django.utils.feedgenerator import Atom1Feed
from models import Entry
from django.conf import settings

set_title = getattr(settings, 'FEEDTITLE', 'Simpleblog latest 10 entries')
set_descr = getattr(settings, 'FEEDDESCR', 'Simpleblog rss news feed')
set_len = getattr(settings, 'FEEDLENGTH', 10)

class RSSLatestEntries(Feed):
    title = set_title
    link = '/news/'
    description = set_descr

    def items(self):
        return Entry.objects.order_by('-created')[:set_len]

class AtomLatestEntries(RSSLatestEntries):
    feed_type = Atom1Feed
    subtitle = RSSLatestEntries.description

