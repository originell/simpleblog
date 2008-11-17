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
                *Default:* ['codehilite', 'tables']

*Note:* If you don't want categories you need to set CATEGORIES to False **before** the initial syncdb. Otherwise you'll need perform the sql changes manually or by using one of the nice db altering utilities for django (django-evolution_, South_, dmigration_,...)

Help
====

+ Here_ you can read how to use syntax highlighting in a post

+ Pygments Syntax CSS Style example (from django-debug-toolbar)::

    .err { color: #ffffff } /* Error */
    .g { color: #ffffff } /* Generic */
    .k { color: #F7C757; font-weight: bold } /* Keyword */
    .o { color: #ffffff } /* Operator */
    .n { color: #ffffff } /* Name */
    .mi { color: #92ef3f; font-weight: bold } /* Literal.Number.Integer */
    .l { color: #ffffff } /* Literal */
    .x { color: #ffffff } /* Other */
    .p { color: #ffffff } /* Punctuation */
    .m { color: #92ef3f; font-weight: bold } /* Literal.Number */
    .s { color: #0086d2 } /* Literal.String */
    .w { color: #888888 } /* Text.Whitespace */
    .il { color: #92ef3f; font-weight: bold } /* Literal.Number.Integer.Long */

+ To get the leatest entry you just have to do the following in a template::

    {% load latest %}
    ....
    {% latest_entry as [varname] %}

.. _pygments: http://pygments.org/
.. _docutils: http://docutils.sourceforge.net/
.. _python: http://www.python.org/
.. _django: http://www.djangoproject.com/
.. _django-evolution: http://code.google.com/p/django-evolution/
.. _South: http://south.aeracode.org/
.. _dmigration: http://code.google.com/p/dmigrations/
.. _markdown: http://www.freewisdom.org/projects/python-markdown/
.. _extensions: http://www.freewisdom.org/projects/python-markdown/Available_Extensions
.. _Here: http://www.freewisdom.org/projects/python-markdown/CodeHilite
