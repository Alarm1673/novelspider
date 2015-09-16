# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

from scrapy import Item,Field


class NovelspiderItem(Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    bookName = Field()      #书名
    bookTitle = Field()     #标题
    chapterNum = Field()    #章节数
    chapterName = Field()   #章节名
    chapterURL = Field()    #章节URL
