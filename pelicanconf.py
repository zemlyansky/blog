#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Anton Zemlyansky'
SITENAME = u'Anton Zemlyansky blog'
SITEURL = 'http://zemlyansky.com/blog'

PATH = 'content'
OUTPUT_PATH = 'docs'

TIMEZONE = 'Europe/Kiev'

DEFAULT_LANG = u'ru'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Pelican', 'http://getpelican.com/'),
         ('Python.org', 'http://python.org/'),
         ('Jinja2', 'http://jinja.pocoo.org/'),
         ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('You can add links in your config file', '#'),
          ('Another social link', '#'),)

DEFAULT_PAGINATION = 10

MARKUP = ('md', 'ipynb')

PLUGIN_PATHS = ['./plugins']
PLUGINS = ['ipynb.markup']

THEME = 'themes/minimalxy'

MINIMALXY_START_YEAR = 2018

# Author
AUTHOR_INTRO = u'Блог Антона Землянского'
AUTHOR_DESCRIPTION = u'Hello world! I’m John Doe. I like coffee, birds and Python.'
AUTHOR_AVATAR = 'http://www.gravatar.com/avatar/abcdefghijkl?s=240'

IGNORE_FILES = ['*-checkpoint.ipynb']
# IPYNB_USE_METACELL = True

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
