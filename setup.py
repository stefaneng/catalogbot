from setuptools import setup, find_packages


setup(
    name='catalogbot',
    version='1.0',
    packages=find_packages(exclude=("tests")),
    entry_points={'scrapy': ['settings = catalogbot.settings']},
    dependency_links = [
        'https://github.com/sprij/scrapy-rethinkdb/tarball/master#egg=scrapy-rethinkdb-1.0.0'
    ],
    install_requires = [
        'nose',
        'scrapy==0.22.2',
        'scrapy-rethinkdb==1.0.0'
    ],
    test_suite = 'nose.collector',
)
