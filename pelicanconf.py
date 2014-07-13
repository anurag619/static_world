#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Anurag'
SITENAME = u'Static_World'
SITEURL = 'http://blog.anuragkr.in'

#Navigation sections and relative URL:
SECTIONS = [('About', 'howdy.html') ,
			('category', 'categories.html'),

			]

DEFAULT_CATEGORY = 'Uncategorized'
DATE_FORMAT = {
'en': '%d %m %Y'
}
DEFAULT_DATE_FORMAT = '%d %m %Y'

OUTPUT_PATH = 'output'

STATIC_PATHS = ['images', 'extra/CNAME']
EXTRA_PATH_METADATA = {'extra/CNAME': {'path': 'CNAME'},}


ARTICLE_URL = ('{slug}/')
ARTICLE_SAVE_AS = ('{slug}.html')
PAGE_URL = ('{slug}/')
PAGE_SAVE_AS = ('{slug}.html')
AUTHOR_URL = ('author/{name}/')
TAG_URL = ('tag/{name}/')

TIMEZONE = 'Asia/Kolkata'

DEFAULT_LANG = u'en'


TWITTER_USERNAME = 'ak_8085'
GITHUB_URL = 'http://github.com/anurag619'

DEFAULT_PAGINATION = 10

DISPLAY_PAGES_ON_MENU = True

PATH = 'content'
PAGE_DIR = 'pages'

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True

# Formatting for dates

DEFAULT_DATE_FORMAT = ('%a %d %B %Y')

# Formatting for urls

ARTICLE_URL = "posts/{date:%Y}/{date:%m}/{slug}/"
ARTICLE_SAVE_AS = "posts/{date:%Y}/{date:%m}/{slug}/index.html"

PAGE_URL =  "{slug}.html"
PAGE_SAVE_AS = '{slug}.html'

CATEGORY_URL = "category/{slug}"
CATEGORY_SAVE_AS = "category/{slug}/index.html"

TAG_URL = "tag/{slug}/"
TAG_SAVE_AS = "tag/{slug}/index.html"

# Generate yearly archive

YEAR_ARCHIVE_SAVE_AS = 'posts/{date:%Y}/index.html'

# Show most recent posts first

NEWEST_FIRST_ARCHIVES = True

# Specify theme

THEME = "content/theme/flasky"

DISPLAY_PAGES_ON_MENU= 'About'
DISQUS_SITENAME = "static-world"
