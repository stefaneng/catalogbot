from scrapy.spider import Spider
from scrapy.http import Request
from scrapy.selector import Selector
from catalogbot.items import CourseItem
from catalogbot.parsetools.courseparser import *

class CatalogSpider(Spider):
    name = "catalog"
    allowed_domains = ["catalog.csun.edu"]
    start_urls = [
        "http://catalog.csun.edu/"
    ]

    def parse_course(self, response):
        sel = Selector(response)

        for course_title_sel in sel.xpath('//div[@id="courses"]/h4'):
            course = CourseItem()

            # Get the title line of course from the <h4>'s
            title = course_title_sel.xpath('text()').extract()[0]

            # Get the course body
            ptag = course_title_sel.xpath('following-sibling::p')
            em = ptag.xpath('em/text()').extract()
            pbody = course_title_sel.xpath('following-sibling::p/text()').extract()[0]

            if len(em) > 0:
                body = em[0] + pbody
            else:
                body = pbody

            course = parse_title(course, title)
            course = parse_prereqs(course, body)
            course = parse_coreqs(course, body)
            course = parse_body(course, pbody)

            yield course

    def parse(self, response):
        sel = Selector(response)

        for url in sel.xpath('//div[@class="cols"]/ul/li/a/@href').extract():
            yield Request(url + 'courses/', callback=self.parse_course)
