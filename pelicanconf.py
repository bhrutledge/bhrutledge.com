#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Brian Rutledge'
SITENAME = u'Brian H. Rutledge'
SITEURL = 'http://bhrutledge.dev'
OUTPUT_PATH = '/Users/brian/Sites/bhrutledge'

TIMEZONE = 'America/New_York'
DEFAULT_LANG = u'en'

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None

THEME = "theme"
DIRECT_TEMPLATES = ('index', 'archives',)
DEFAULT_DATE_FORMAT = "%B %d, %Y"
DEFAULT_PAGINATION = 10
TYPOGRIFY = True

PAGE_URL = '{slug}/'
PAGE_SAVE_AS = '{slug}/index.html'
ARTICLE_URL = '{date:%Y}/{date:%m}/{slug}/'
ARTICLE_SAVE_AS = '{date:%Y}/{date:%m}/{slug}/index.html'
ARCHIVES_SAVE_AS = 'archive/index.html'
CATEGORY_URL = 'category/{slug}/'
#CATEGORY_SAVE_AS = 'category/{slug}/index.html'
CATEGORY_SAVE_AS = False
TAG_URL = 'tag/{slug}/'
#TAG_SAVE_AS = 'tag/{slug}/index.html'
TAG_SAVE_AS = False
AUTHOR_URL = 'author/{slug}/'
#AUTHOR_SAVE_AS = 'author/{slug}/index.html'
AUTHOR_SAVE_AS = False

