"""
Assists in parsing text from the course pages.
"""
import re
from catalogbot.items import CourseItem

def parse_title(courseitem, title):
    """
    Take a class title and divide into courseitem
    """

    split_title = title.split(' ')
    classname = " ".join(split_title[:2]).strip('.')
    rest_title = " ".join(split_title[2:])
    longname = rest_title.split('(')[0].strip()

    m = re.search(r'\((.*)\)', rest_title)
    if m:
        courseitem['units'] = m.group(1)

    (dep, number) = classname.split(' ')

    courseitem['classname'] = classname
    courseitem['department'] = dep
    courseitem['number'] = number
    courseitem['longname'] = longname

    return courseitem

def parse_body(courseitem, body):
    courseitem['description'] = body
    return courseitem
