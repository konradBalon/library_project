# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy
from itemloaders.processors import MapCompose
from scrapy import Item, Field
from scrapy.loader.processors import TakeFirst, Join
from w3lib.html import remove_tags

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
    description = Field(output_processor=Join(),)
    pages = Field(output_processor=TakeFirst(),)


