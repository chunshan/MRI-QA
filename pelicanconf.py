#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

#Site basic settings
AUTHOR = u'Chunshan'
AUTHOR_EMAIL = u"shan.c.young@gmail.com"
SITENAME = u'MRI Q&A'
SITEURL = 'http://chunshan.github.io/MRI-QA'
DEFAULT_METADATA = (
)
DELETE_OUTPUT_DIRECTORY = False
USE_FOLDER_AS_CATEGORY = True
PATH = 'content'

# Regional Settings
TIMEZONE = 'Asia/Shanghai'
DEFAULT_DATE_FORMAT = ('%Y-%m-%d')
DEFAULT_LANG = u'zh'

# plugins and extensions settings
PLUGINS = ['sitemap', 'extract_toc', 'tipue_search']
PLUGIN_PATHS = [u"pelican-plugins",]

SITEMAP = {
    'format': 'xml',
    'priorities': {
        'articles': 0.5,
        'indexes': 0.5,
        'pages': 0.5
        },
    'changefreqs': {
        'articles': 'weekly',
        'indexes': 'daily',
        'pages': 'monthly'
        }
    }

#theme settings
THEME = 'pelican-elegant'
DIRECT_TEMPLATES = (('index', 'tags', 'categories','archives', 'search', '404'))
STATIC_PATHS = ['theme/images', 'images']

# Landing Page
PROJECTS = [
        {
            "name": "MRI Q&A",
            "url": "http://chunshan.github.io/MRI-QA",
            "description": """<div>This project translates some articles in <a href="http://mriquestions.com/"
			title="Questions and Answers in MRI" itemprop="affiliation">Questions and Answers in MRI</a></div>"""},
        ]
LANDING_PAGE_ABOUT = {"title": "磁共振知识问答 - MRI Q&A",
        "details": "Updating..."}

# URL settings
ARTICLE_URL = '{category}/{slug}.html'
ARTICLE_SAVE_AS = ARTICLE_URL
PAGE_URL = '{slug}.html'
PAGE_SAVE_AS = PAGE_URL
CATEGORY_URL = '{slug}/index.html'
CATEGORY_SAVE_AS = CATEGORY_URL
TAG_SAVE_AS = ""

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Pelican', 'http://getpelican.com/'),
         ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('You can add links in your config file', '#'),
          ('Another social link', '#'),)

# pagination settings		  
DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True