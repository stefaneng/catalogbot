from setuptools import setup, find_packages


setup(
    name='catalogbot',
    version='1.0',
    packages=find_packages(exclude=("tests")),
    entry_points={'scrapy': ['settings = catalogbot.settings']},
    install_requires = [r.strip('\n') for r in open('requirements.txt')],
    dependency_links=['https://github.com/sprij/scrapy-rethinkdb/tarball/master#egg=package-1.0'],
    test_suite = 'nose.collector',
)
