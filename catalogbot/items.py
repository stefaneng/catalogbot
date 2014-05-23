# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

from scrapy.item import Item, Field

class CourseItem(Item):
    name = Field()
    number = Field()
    units = Field()
    prereqs = Field()
    coreqs = Field()
    statisfies = Field()
