import scrapy
from scrapy.loader import ItemLoader

from crawler.items import BookItem


class BooksSpider(scrapy.Spider):
    name = 'books'
    allowed_domains = ['www.lubimyczytac.pl', 'lubimyczytac.pl']
    start_urls = ['https://lubimyczytac.pl/katalog']

    def parse(self, response):
        books_url = response.xpath("//a[@class='authorAllBooks__singleTextTitle float-left']/@href").getall()
        print(books_url)
        for url in books_url:
            yield scrapy.Request(url=f'https://www.lubimyczytac.pl{url}', callback=self.parse_book)

        next_page = response.xpath("//a[@class='page-link ml-0 stdPaginator btn']").xpath('@data-page').get()

        if next_page is not None:
            next_page = response.urljoin(f'?page={next_page}')
            print(f'{next_page}' * 20)
            yield scrapy.Request(next_page, callback=self.parse)

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
        l.add_xpath('description', "//div[@class='collapse-content']//p//text()")
        l.add_xpath('pages',
                    "//span[@class='d-sm-inline-block book-pages book__pages pr-2 mr-2 pr-sm-3 mr-sm-3']/text()")

        return l.load_item()
