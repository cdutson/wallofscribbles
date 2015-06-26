#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals
import datetime

AUTHOR = u'Corey Dutson'
SITENAME = u'Wall Of Scribbles'
SITEURL = ''
THEME = 'themes/white-n-green/'

DIRECT_TEMPLATES = ['index', 'archives', 'tags']
PAGINATED_DIRECT_TEMPLATES = ['archives', 'tags']
SUMMARY_MAX_LENGTH=120

PATH = 'content'
PAGE_PATHS = ['pages']
ARTICLE_PATHS = ['articles', 'portfolio']

PORTFOLIO_CATEGORY = 'portfolio'

TIMEZONE = 'America/Toronto'

DEFAULT_LANG = u'en'
CURRENT_DATE = datetime.datetime.now()

PATH_METADATA = '\A(?P<date>\d{4}/\d{2}/)-(?P<slug>.*)(.md|.rst)'
#ARTICLE_URL = '{date:%Y}/{date:%m}/{slug}/'
ARTICLE_URL = '{date:%Y}/{date:%m}/{slug}.html'
ARTICLE_SAVE_AS = '{date:%Y}/{date:%m}/{slug}.html'
STATIC_PATHS = ['images', 'wp-content', 'downloads']

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
SOCIAL = (('Twitter', 'https://twitter.com/cdutson'),)


DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True

PLUGIN_PATHS = ['plugins']
PLUGINS = ['gzip_cache', 'neighbors', 'post_stats', 'sitemap', 'assets', 'summary',]

#EXCLUDE_CATEGORIES = ['portfolio',]

DISQUS_SITENAME = "wallofscribbles"

# Sitemap Settings
SITEMAP = {
    'format': 'xml',
    'priorities': {
        'articles': 0.8,
        'portfolio)items':0.5,
        'indexes': 0.5,
        'pages': 0.5
    },
    'changefreqs': {
        'articles': 'monthly',
        'indexes': 'daily',
        'pages': 'monthly',
        'portfolio_items': 'monthly',
    }
}