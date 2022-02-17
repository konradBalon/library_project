# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy import Item, Field
from scrapy.loader import ItemLoader
from scrapy.loader.processors import TakeFirst


class CrawlerItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass


class BookItem(Item):
    title = Field(output_processor=TakeFirst(),)
    author = Field(output_processor=TakeFirst(),)
    author_url = Field(output_processor=TakeFirst(),)
    publisher = Field(output_processor=TakeFirst(),)
    category = Field(output_processor=TakeFirst(),)
    book_url = Field(output_processor=TakeFirst(),)
    book_img = Field(output_processor=TakeFirst(),)


