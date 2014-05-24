"""
Assists in parsing text from the course pages.
"""
import re
from itertools import chain

def parse_title(courseitem, title):
    """
    Take a class title and divide into courseitem
    """

    split_title = title.split(' ')

    if len(split_title) <= 1:
        return courseitem

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

def parse_comma_string(comma_string):
    components = comma_string.split(',')
    first = components[0]
    name = first.split(' ')[0]

    name_number_list = [first] + [''.join([name, comp]) for comp in components[1:]]

    return name_number_list

def parse_em(courseitem, req_name, em_string):
    m = re.search(r':(.*?)\.', em_string)
    if m:
        preq_string = m.group(1).strip(' ')
    else:
        return courseitem

    prereqs = [parse_comma_string(c.strip(' '))
               for c in preq_string.split(';')]

    courseitem[req_name] = list(chain.from_iterable(prereqs))

    return courseitem

def parse_coreqs(courseitem, body):
    coreq_string = parse_coreqs_body(body)
    courseitem = parse_em(courseitem, 'coreqs', coreq_string)
    return courseitem

def parse_prereqs(courseitem, body):
    prereq_string = parse_prereqs_body(body)
    courseitem = parse_em(courseitem, 'prereqs', prereq_string)
    return courseitem

def parse_prep(courseitem, body):
    prep_string = parse_prep_body(body)
    courseitem = parse_em(courseitem, 'prep', prep_string)
    return courseitem

def parse_coreqs_body(body):
    m = re.search(r'Corequisites{0,1}:.*?\.', body)
    if m is not None:
        return m.group(0)
    else:
        return ''

def parse_prep_body(body):
    m = re.search(r'Preparatory:.*?\.', body)
    if m is not None:
        return m.group(0)
    else:
        return ''


def parse_prereqs_body(body):
    m = re.search(r'Prerequisites{0,1}:.*?\.', body)
    if m is not None:
        return m.group(0)
    else:
        return ''

def parse_body(courseitem, body):
    m = re.search(r'Prerequisites{0,1}:.*?\.\ (.*)', body)
    if m is not None:
        body = m.group(1)

    m2 = re.search(r'Corequisites{0,1}:.*?\.\ (.*)', body)
    if m2 is not None:
        body = m2.group(1)

    m3 = re.search(r'Preparatory:.*?\.\ (.*)', body)
    if m3 is not None:
        body = m3.group(1)

    courseitem['description'] = body
    return courseitem
