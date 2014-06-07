from setuptools import setup, find_packages


setup(
    name='catalogbot',
    version='1.0',
    packages=find_packages(exclude=("tests")),
    entry_points={'scrapy': ['settings = catalogbot.settings']},
    install_requires = [r.strip('\n') for r in open('requirements.txt')],
    test_suite = 'nose.collector',
)
