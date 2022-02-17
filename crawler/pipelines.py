# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter


class CrawlerPipeline:
    def process_item(self, item, spider):
        return item


class BookPipeline:
    def process_item(self, item, spider):
        adapter = ItemAdapter(item)
        for key in adapter:
            adapter[key] = adapter[key].replace("\n","").strip()
        return item
