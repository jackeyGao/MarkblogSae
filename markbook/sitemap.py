# -*- coding: utf-8 -*-
'''
File Name: markbook/sitemap.py
Author: JackeyGao
mail: junqi.gao@shuyun.com
Created Time: 三  5/ 6 21:49:09 2015
'''
from django.contrib.sitemaps import Sitemap
from blog.models import Entry

class BlogSitemap(Sitemap):
    changefreq = "daily"
    priority = 0.5

    def items(self):
        return Blog.objects.filter(is_draft=False)

    def lastmod(self, obj):
        return obj.created_time
