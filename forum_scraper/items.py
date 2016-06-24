# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class ForumScraperItem(scrapy.Item):

	Title = scrapy.Field()
	Author = scrapy.Field()
	Content = scrapy.Field()
	Category = scrapy.Field()
	Tags = scrapy.Field()