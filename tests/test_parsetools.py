from catalogbot.parsetools import courses
from catalogbot.items import CourseItem

def test_parse_title():
    courseItem = CourseItem()
    courseItem['classname'] = 'COMP 310'
    courseItem['department'] = 'COMP'
    courseItem['number'] = '310'
    courseItem['longname'] = 'Automata, Languages and Computation'
    courseItem['units'] = '3'

    coursetitle = 'COMP 310. Automata, Languages and Computation (3)'
    out_courseItem = courses.parse_title(courseItem, coursetitle)
    assert courseItem == out_courseItem
