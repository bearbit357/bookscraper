import scrapy
from bookscraper.items import BookscraperItem


class BookspiderSpider(scrapy.Spider):
    name = "bookspider"
    allowed_domains = ["books.toscrape.com"]
    start_urls = ["https://books.toscrape.com"]

    def parse(self, response):
        books = response.css('article.product_pod')
        for book in books:
            book_url = book.css('h3 a').attrib['href']
            yield response.follow(book_url,callback = self.book_parse)
        next_page = response.css('li.next a').attrib['href']
        if next_page is not None:
            yield response.follow(next_page,callback=self.parse)
    

    def book_parse(self,response):
        book_item = BookscraperItem()
        book_item['title']=response.css('.row h1::text').get()
        book_item['price']=response.css('.price_color::text').get()
        book_item['stars']=response.css('.star-rating').attrib['class']
        book_item['stock']=response.css('.instock::text').getall()
        yield book_item
