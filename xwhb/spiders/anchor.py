import scrapy


class AnchorSpider(scrapy.Spider):
    name = "anchor"
    custom_settings = {
        "DOWNLOAD_HANDLERS": {
            "https": "scrapy_playwright.handler.ScrapyPlaywrightDownloadHandler",
            "http": "scrapy_playwright.handler.ScrapyPlaywrightDownloadHandler",
        },
    }
    start_urls = ["https://www.news.cn/"]

    async def start(self):
        for url in self.start_urls:
            yield scrapy.Request(url=url, meta={"playwright": True})

    def parse(self, response):
        for href in response.css("a::attr(href)").getall():
            abs_url = response.urljoin(href)
            yield {"url": abs_url}
