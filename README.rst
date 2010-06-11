=================
django-simpleblog
=================

--
is
--

the blogengine behind origiNell_. My aim is to keep it, as the name suggests, simple, fast and easy to integrate/customize.

Requirements
============

* pygments_ >= 0.10
* markdown_

and of course

+ python_ >= 2.3
+ django_ >= 1.2

Installation
============

Use the included setup.py

::

    python setup.py install

Then open up your project's urls.py and include this app's urls.
For example:

::

    (r'^blog/', include('django_simpleblog.urls.entries')),

Options
=======

You can specify the following options in your settings.py:
    - **TAGGING**
                If True, tags will be enabled. There's a check if django-tagging is installed. If so, then we'll use that as tagfield, otherwise tags will be handled as plain-text.
                *Default:* True
    - **CATEGORIES**
                   If True, category support will be enabled.
                   *Default:* True
    - **MARKDOWN**
                If True, this will enable Markdown markup language.
                *Default:* True
    - **MARKDOWN_EXTS**
                A list containing available markdown extensions_
                *Default:* ['codehilite',]
    - **COMMENTS**
                If True enables django's comments framework
                *Default:* True
    - **COMMENTS_NOTIFICATION**
                If True enables email notification about new comments
                *Default:* False
    - **COMMENTS_MODERATION**
                If True, a comment containing the <a href=..> html tag, will NOT be displayed on the website.
                It's is_public attribute will therefore be set to False.
                *Default:* True

*Note:* If you don't want categories you need to set CATEGORIES to False **before** the initial syncdb. Otherwise you'll need perform the sql changes manually or by using one of the nice db altering utilities for django (django-evolution_, South_, dmigration_,...)

RSS/Atom Feeds
==============

To enable RSS/Atom feeds simply add the following to your urls.py:

::

    (r'^feeds/', include('django_simpleblog.urls.feeds')),

This will enable two feeds: latest entries and if you set CATEGORIES to true, a category based feed.

Feeds can be customized via the FEED_SETTINGS dictionary in your settings.py. Here are the default settings. If you didn't activate CATEGORIES, ignore the 'category' part.

::

    FEED_SETTINGS = {'latest': {'title': 'Simpleblog Latest 10 Entries',
                                'link':  '/news/',
                                'description': 'Simpleblog Newsfeed',
                                'length': 10,
                                'item_descr_length': 48,},
                     'category': {'title': 'Simpleblog Categoryfeed',
                                  'link': '/category/',
                                  'description': 'Feed For Category "%s"'},
                    }

Note that %s in category title and description will be replaced by the categoryname, if specified.
                    

Comment Moderation
==================

We now have a simple option to moderate an entry based on it's content. Thanks to django\'s very flexible comments framework, it's a breeze (see admin.py):

::

        class EntryModerator(CommentModerator):
            email_notification = COMMENTS_NOTIFICATION
            enable_field = \'enable_comments\'

            if COMMENTS_MODERATION:
                def moderate(self, comment, content_object, request):
                    if self.auto_moderate_field and self.moderate_after:
                        if self._get_delta(datetime.datetime.now(), getattr(content_object, self.auto_moderate_field)).days >= self.moderate_after:
                            return True
                    if 'a href' in comment.comment:
                        return True
                    return False
        moderator.register(Entry, EntryModerator)

As you can see right now we simply check for 'a href' in a comment. This is the most used html tag I've seen in spam.
Anyway, you may have noticed that you can actually have access to the comment object, content_object and request. This of course enables a hell lot of ways to refine spam protection (or you just tie Akismet in at this point).

*Note:* "if 'a href' in" is **not** case insensitive. If you want case insensitivity you either have to do lower(comment.comment) or use a regular expression.

A little tip for everyone who wants the user, or rather say spambot, to know that his/her comment has been moderated.
I bet you already customised *comments/posted.html* to fit your need. Notice that you actually have full access to the comment itself inside this template!

Here's what I did:

::

    {% if comment.is_public %}
        <h1>{% trans "Thank you for your comment" %}.</h1><br />
        <a href="{{ comment.get_absolute_url }}">View it!</a>
    {% else %}
        <h1>Your comment has been moderated because of denied usage of HTML</h1><br />
        It must be reviewed and approved by the admin.
    {% endif %}
    
If you need more advanced spam protection, I suggest you take a look at akismet integration in django. There are a lot of blog posts about it.
In case you want to outsource comments, I highly recommend you take a look at Disqus_ in combination with django-disqus_. I have also blogged about the comment migration.

Templatetags
============

human_enum
----------

Creates a humanized enumeration of a specified queryset.

Usage::

    {% human_enum YourQueryset %}

or if you want to have urls to the object::

    {% human_enum YourQueryset urlify %}

The __unicode__() method in your model should return some kind of title
of your object.
If you enable the option to build urls, your model needs a get_absolute_url()
method.

Help
====

+ How_ to use syntax highlighting in a post

+ See how to generate a css for pygment's here_

+ To get the latest entry you just have to do the following in a template::

    {% load latest %}
    ....
    {% latest_entry as [varname] %}

+ Check if an entry has been modified

    {% ifnotequal object.created object.modified %}..{% endifnotequal %}

.. _pygments: http://pygments.org/
.. _docutils: http://docutils.sourceforge.net/
.. _python: http://www.python.org/
.. _django: http://www.djangoproject.com/
.. _django-evolution: http://code.google.com/p/django-evolution/
.. _South: http://south.aeracode.org/
.. _dmigration: http://code.google.com/p/dmigrations/
.. _markdown: http://www.freewisdom.org/projects/python-markdown/
.. _extensions: http://www.freewisdom.org/projects/python-markdown/Available_Extensions
.. _How: http://www.freewisdom.org/projects/python-markdown/CodeHilite
.. _here: http://pygments.org/docs/cmdline/#generating-styles
.. _origiNell: http://www.originell.org/
.. _Disqus: http://disq.us/
.. _django-disqus: http://github.com/arthurk/django-disqus