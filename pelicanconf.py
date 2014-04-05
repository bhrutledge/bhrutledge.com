#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Brian Rutledge'
SITENAME = u'Brian H. Rutledge'
SITEURL = 'http://bhrutledge.dev'

TIMEZONE = 'America/New_York'
DEFAULT_LANG = u'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None

THEME = 'theme'
DIRECT_TEMPLATES = ('index',)
STATIC_PATHS = ['images', 'photos', 'extra']
PLUGIN_PATH = '../pelican-plugins'
PLUGINS = ['neighbors']

USE_FOLDER_AS_CATEGORY = False
DEFAULT_DATE = "fs"
FILENAME_METADATA ='(?P<slug>.*)'
DEFAULT_DATE_FORMAT = "%B %d, %Y"
DEFAULT_PAGINATION = False
TYPOGRIFY = True

EXTRA_PATH_METADATA = {
    'extra/htaccess': {'path': '.htaccess'},
}
ARTICLE_URL = '{slug}'
DRAFT_URL = 'drafts/{slug}'
PAGE_URL = 'pages/{slug}'
ARCHIVES_SAVE_AS = False
CATEGORY_SAVE_AS = False
TAG_SAVE_AS = False
AUTHOR_SAVE_AS = False
