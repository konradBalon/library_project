import scrapy
from scrapy.loader import ItemLoader

from crawler.items import BookItem


class BooksSpider(scrapy.Spider):
    name = 'books'
    allowed_domains = ['www.lubimyczytac.pl/katalog', 'www.lubimyczytac.pl']
    start_urls = ['https://lubimyczytac.pl/katalog/']

    def parse(self, response):
        books_url = response.xpath("//a[@class='authorAllBooks__singleTextTitle float-left']/@href").getall()
        print(books_url)
        for url in books_url:
            yield scrapy.Request(url=f'https://www.lubimyczytac.pl{url}', callback=self.parse_book)

    def parse_book(self, response):
        l = ItemLoader(item=BookItem(), response=response)

        l.add_xpath('title', "//h1[@class='book__title']//text()")
        l.add_xpath('author', "//a[@class='link-name']/text()")
        l.add_xpath('author_url', "//a[@class='link-name']/@href")
        l.add_xpath('publisher', "//span[@class='book__txt d-block d-xs-none mt-2 ']/a/text()")
        l.add_xpath('category', "//a[@class='book__category d-sm-block d-none']/text()")
        l.add_xpath('title', "//h1[@class='book__title']//text()")
        l.add_xpath('book_img', "//img[@class='img-fluid']/@src")
        l.add_value('book_url', response.url)


        # title = response.xpath("//h1[@class='book__title']//text()").extract()[0].strip()
        # author = response.xpath("//a[@class='link-name']/text()").extract()[0].strip()
        # author_url = response.xpath("//a[@class='link-name']/@href").get()
        # publisher = response.xpath("//span[@class='book__txt d-block d-xs-none mt-2 ']/a/text()").extract()[0].strip()
        # category = response.xpath("//a[@class='book__category d-sm-block d-none']/text()").extract()[0].replace("\n",
        #                                                                                                         "").strip()
        return l.load_item()
