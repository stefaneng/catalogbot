from catalogbot.parsetools import courseparser
from catalogbot.items import CourseItem

def test_parse_remove_prereqs():
    """Removed the prereq string from body: 'Prerequisite: COMP 490/L. Project-oriented lab to allow students to complete the design, implementation and testing of the team-based software engineering project started in COMP 490/L. Lab: 3 hours per week.'"""

    body = 'Prerequisite: COMP 490/L. Project-oriented lab to allow students to complete the design, implementation and testing of the team-based software engineering project started in COMP 490/L. Lab: 3 hours per week.'

    courseitem = CourseItem()
    target_string = 'Project-oriented lab to allow students to complete the design, implementation and testing of the team-based software engineering project started in COMP 490/L. Lab: 3 hours per week.'
    courseitem['description'] = target_string
    out_item = courseparser.parse_body(CourseItem(), body)

    print courseitem, out_item

    assert courseitem == out_item

def test_parse_body_to_prereqs():
    """Tests 'Prerequisites: COMP 182/L; MATH 150A; PHIL 230. Study of discrete mathematical structures and proof techniques as used in computer science. Discrete structures, such as functions, relations, sets, graphs and trees. Proof techniques, such as proof by induction, proof by contradiction and proof by cases. Counting techniques. Lab: 3 hours per week.'"""

    body = 'Prerequisites: COMP 182/L; MATH 150A; PHIL 230. Study of discrete mathematical structures and proof techniques as used in computer science. Discrete structures, such as functions, relations, sets, graphs and trees. Proof techniques, such as proof by induction, proof by contradiction and proof by cases. Counting techniques. Lab: 3 hours per week.'
    target_string = 'Prerequisites: COMP 182/L; MATH 150A; PHIL 230.'
    out_string = courseparser.parse_prereqs_body(body)

    print target_string, out_string
    assert target_string == out_string

def test_parse_prereqs():
    """Test parsing of prerequisites 'Prerequisites: COMP 256/L, 333.'"""

    courseitem = CourseItem()
    courseitem['prereqs'] = ['COMP 256/L', 'COMP 333']
    em_tag = 'Prerequisites: COMP 256/L, 333.'
    out_courseitem = courseparser.parse_em(CourseItem(), em_tag)

    print courseitem, out_courseitem

    assert courseitem == out_courseitem

def test_parse_prereq_semicolons():

    test_string = 'Prerequisites: COMP 182/L; MATH 150A; PHIL 230.'
    courseitem = CourseItem()
    courseitem['prereqs'] = ['COMP 182/L', 'MATH 150A', 'PHIL 230']
    out_courseitem = courseparser.parse_em(CourseItem(), test_string)

    print courseitem, out_courseitem

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
