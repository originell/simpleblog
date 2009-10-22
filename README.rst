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

*Note:* If you don't want categories you need to set CATEGORIES to False **before** the initial syncdb. Otherwise you'll need perform the sql changes manually or by using one of the nice db altering utilities for django (django-evolution_, South_, dmigration_,...)

Help
====

+ How_ to use syntax highlighting in a post

+ See how to generate a css for pygment's here_

+ To get the leatest entry you just have to do the following in a template::

    {% load latest %}
    ....
    {% latest_entry as [varname] %}

+ Check if an entry has been modified

    {% if [varname].was_modified %}..{% endif %}

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
