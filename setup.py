from setuptools import setup, find_packages
from pip.req import parse_requirements

setup(
    name='catalogbot',
    version='1.0',
    packages=find_packages(exclude=("tests")),
    entry_points={'scrapy': ['settings = catalogbot.settings']},
    install_requires = [
        str(install_req.req)
        for install_req in parse_requirements('requirements.txt')
    ],
    test_suite = 'nose.collector',
)
