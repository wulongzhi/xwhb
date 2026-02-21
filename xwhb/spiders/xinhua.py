import scrapy


class XinhuaSpider(scrapy.Spider):
    name = "xinhua"
    start_urls = ["https://www.news.cn/"]

    def parse(self, response):
        for href in response.css("a::attr(href)").getall():
            if href.split("/")[-1] == "c.html":
                yield {"url": response.url, "c_html": href}
                yield response.follow(href, self.parse)
            else:
                yield {"url": response.url, "href": href}
