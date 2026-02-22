import scrapy


class AnchorSpider(scrapy.Spider):
    name = "anchor"
    start_urls = ["https://www.news.cn/"]

    def parse(self, response):
        for href in response.css("a::attr(href)").getall():
            abs_url = response.urljoin(href)
            yield {"url": abs_url}
