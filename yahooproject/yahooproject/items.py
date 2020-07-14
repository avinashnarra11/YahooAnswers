# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class YahooprojectItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    #qid = scrapy.Field()
    #categoryname = scrapy.Field()
    user_name = scrapy.Field()
    answer = scrapy.Field()
    comments = scrapy.Field()
    date = scrapy.Field()
    likes = scrapy.Field()
    dislikes = scrapy.Field()
    # answerer_nickname = scrapy.Field()
    # answerer_kid = scrapy.Field()
    # user_canComment = scrapy.Field()
    # user_canChooseBestAnswer = scrapy.Field()
    # user_canFlag = scrapy.Field()
    # user_canVote = scrapy.Field()
    # user_hasCommented = scrapy.Field()
    # user_hasFlagged = scrapy.Field()
    # user_hasVoted = scrapy.Field()
    # user_isAuthor = scrapy.Field()
    # isBestAnswer = scrapy.Field()
    # isAnonymous = scrapy.Field()
    # commentCount = scrapy.Field()





