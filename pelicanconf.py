#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'SaveTFP'
SITENAME = 'SaveTFP'
SITEURL = ''

PATH = 'content'
TIMEZONE = 'America/New_York'
DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

DEFAULT_PAGINATION=10

DISPLAY_PAGES_ON_MENU = False
DISPLAY_CATEGORIES_ON_MENU = False
MENUITEMS = [
    ('Events', '/events/'),
    ('Members', '/members/'),
    # ('Join', '/join/'),
    ('About', '/about/'),
]

INDEX_SAVE_AS = "blog_index.html"
PAGE_PATHS = ['pages']
PAGE_URL="{slug}/"
PAGE_SAVE_AS="{slug}/index.html"

LINKS = (
    ('AODS', 'https://studentlife.mit.edu/aods'),
)

# Social widget
SOCIAL = [
    ('Email Us', 'mailto:savetfp@mit.edu' ),
]


PLUGINS = ['pelican_alias']
