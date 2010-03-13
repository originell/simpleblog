=================
django-simpleblog
=================

--
is
--

a hopefully simple blog app without too much bloat. Maybe it turns into an *uber-bloated* app, let's see what I'll do with it :-) Basically it's just a practice project.

Requirements
============

* pygments_ >= 0.10
* markdown_

and of course

+ python_ >= 2.3
+ django_ >= 1.0

Options
=======

You can specify the following options in your settings.py:
    - **FEEDTITLE**
                  Sets the title for both RSS and Atom feeds.
                  *Default:* 'Simpleblog latest 10 entries'
    - **FEEDDESCR**
                  Sets the description for both RSS and Atom feeds
                  *Default:* ''Simpleblog rss news feed'
    - **FEEDLENGTH**
                   Sets the number of items available in both RSS and Atom feeds.
                   *Default:* 10
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

Comment Moderation
==================

We now have a simple option to moderate an entry based on it's content. Thanks to django\'s very flexible comments framework, it's a breeze (see admin.py):

        class EntryModerator(CommentModerator):
            email_notification = COMMENTS_NOTIFICATION
            enable_field = 'enable_comments'

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

    {% if comment.is_public %}
        <h1>{% trans "Thank you for your comment" %}.</h1><br />
        <a href="{{ comment.get_absolute_url }}">View it!</a>
    {% else %}
        <h1>Your comment has been moderated because of denied usage of HTML</h1><br />
        It must be reviewed and approved by the admin.
    {% endif %}

Help
====

+ How_ to use syntax highlighting in a post

+ See how to generate a css for pygment's here_

+ To get the leatest entry you just have to do the following in a template::

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
