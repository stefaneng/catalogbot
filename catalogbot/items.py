# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

from scrapy.item import Item, Field

class CourseItem(Item):
    description = Field()
    classname = Field()
    department = Field()
    number = Field()
    longname = Field()
    units = Field()
