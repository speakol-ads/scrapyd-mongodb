#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

setup(
    name='scrapyd-redis',
    version='0.1.1',
    description='Scrapyd Queue Management with Redis',
    author='Tiago Lira',
    author_email='tiagolira.dev@gmail.com',
    license='MIT',
    url='https://github.com/speakol-ads/scrapyd-redis',
    keywords=['scrapy', 'scrapyd', 'redis', 'queue',
              'scrapyd-queue', 'scrapyd-backend', 'backend'],
    include_package_data=True,
    packages=find_packages(),
    install_requires=[
        'scrapy',
        'redis',
    ],
    classifiers=[],
)
