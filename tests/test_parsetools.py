from catalogbot.parsetools import courseparser
from catalogbot.items import CourseItem

def test_parse_prereqs():
    """Test parsing of prerequisites 'Prerequisites: COMP 256/L, 333.'"""

    courseitem = CourseItem()
    courseitem['prereqs'] = ['COMP 256/L', 'COMP 333']
    em_tag = 'Prerequisites: COMP 256/L, 333.'
    out_courseitem = courseparser.parse_em(CourseItem(), em_tag)

    assert courseitem == out_courseitem

def test_parse_title_empty():
    """Test parsing an empty title"""

    courseitem = CourseItem()
    coursetitle = ''
    out_courseitem = courseparser.parse_title(CourseItem(), coursetitle)

    assert courseitem == out_courseitem


def test_parse_title():
    """Parse a class title for 'COMP 310. Automata, Languages and Computation (3)'"""

    courseItem = CourseItem()
    courseItem['classname'] = 'COMP 310'
    courseItem['department'] = 'COMP'
    courseItem['number'] = '310'
    courseItem['longname'] = 'Automata, Languages and Computation'
    courseItem['units'] = '3'

    coursetitle = 'COMP 310. Automata, Languages and Computation (3)'
    out_courseItem = courseparser.parse_title(CourseItem(), coursetitle)

    assert courseItem == out_courseItem
