#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = "Sayantan Khan"
SITENAME = "Sayantan Khan's website"
SITEURL = ""
STATIC_PATHS = ["images", "pages/pdfs"]
THEME = "theme"

PLUGIN_PATHS = ["plugins"]
PLUGINS = ["render_math", "pelican_javascript"]

PATH = "content"

DISPLAY_CATEGORIES_ON_MENU = False
DISPLAY_PAGES_ON_MENU = False

MENUITEMS = (
    ("Research", "/pages/research.html"),
    ("Talks", "/pages/talks.html"),
    ("Notes", "/pages/notes.html"),
    ("Software", "/pages/software.html"),
    ("Blog", "/blog/index.html"),
    ("Contact", "/pages/contact.html"),
    ("CV", "/pages/cv.html"),
)

INDEX_SAVE_AS = "blog/index.html"
INDEX_URL = "blog/"

TIMEZONE = "America/Detroit"

DEFAULT_LANG = "en"

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = []
# ('Pelican', 'http://getpelican.com/'),
# ('Python.org', 'http://python.org/'),
# ('Jinja2', 'http://jinja.pocoo.org/'),
# ('You can modify those links in your config file', '#'),)

# Social widget
# SOCIAL = (('You can add links in your config file', '#'),
# ('Another social link', '#'),)

DEFAULT_PAGINATION = 6

# Uncomment following line if you want document-relative URLs when developing
# RELATIVE_URLS = True
# DISQUS_SITENAME = "sayantan-khans-blog"
