from scrapy.spider import Spider
from scrapy.http import Request
from scrapy.selector import Selector
from catalogbot.items import CourseItem


class CatalogSpider(Spider):
    name = "catalog"
    allowed_domains = ["catalog.csun.edu"]
    start_urls = [
        "http://catalog.csun.edu/"
    ]

    def parse_course(self, response):
        sel = Selector(response)

    def parse(self, response):
        sel = Selector(response)

        for url in sel.xpath('//div[@class="cols"]/ul/li/a/@href').extract():
            yield Request(url + 'courses/', callback=self.parse_course)
