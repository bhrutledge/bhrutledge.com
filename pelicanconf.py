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

THEME = "theme"
DIRECT_TEMPLATES = ('index',)
STATIC_PATHS = ['images', 'photos']
PLUGIN_PATH = '../pelican-plugins'
PLUGINS = ['neighbors', 'img_class']

USE_FOLDER_AS_CATEGORY = False
DEFAULT_DATE = "fs"
FILENAME_METADATA ='(?P<slug>.*)'
DEFAULT_DATE_FORMAT = "%B %d, %Y"
DEFAULT_PAGINATION = False
TYPOGRIFY = True

FILES_TO_COPY = (
    ('extra/htaccess', '.htaccess'),
    ('extra/resume.html', 'resume.html'),
)
PAGE_URL = '{slug}'
PAGE_SAVE_AS = '{slug}.html'
ARTICLE_URL = '{slug}'
ARTICLE_SAVE_AS = '{slug}.html'
ARCHIVES_SAVE_AS = False
CATEGORY_SAVE_AS = False
TAG_SAVE_AS = False
AUTHOR_SAVE_AS = False
