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
* docutils_

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
    - **USE_TAGGING**
                    If True, tags will be enabled. There's a check if django-tagging is installed. If so, then we'll use that as tagfield, otherwise tags will be handled as plain-text.
                    *Default:* True

Help
========

+ To use syntax highlighting in blog entries (replace *python* with any other language)::

    .. sourcecode:: python

       print 'Your code goes here!'

.. _pygments: http://pygments.org/
.. _docutils: http://docutils.sourceforge.net/
.. _python: http://www.python.org/
.. _django: http://www.djangoproject.com/
