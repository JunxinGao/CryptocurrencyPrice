# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class ScrapyItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass

class MxcMarketTickerDataItem(scrapy.Item):
    data = scrapy.Field()

class MxcMarketTickerItem(scrapy.Item):
    symbol = scrapy.Field()
    volume = scrapy.Field()
    high = scrapy.Field()
    low = scrapy.Field()
    bid = scrapy.Field()
    ask = scrapy.Field()
    open = scrapy.Field()
    last = scrapy.Field()
    time = scrapy.Field()
    change_rate = scrapy.Field()