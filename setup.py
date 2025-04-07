#!/usr/bin/env python
# -*- coding: utf-8 -*-


from setuptools import setup, find_packages

setup(
    name='docx',
    version='1.1.2.1',
    package_dir={"": "src"},
    packages=find_packages(where='src'),
    install_requires=[
        "lxml"
    ],
    author='nicefeiniu',
    author_email='872938058@qq.com',
    description='官方python-docx的merge pull requests',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/nciefeiniu/python-docx',
    classifiers=[
        'Programming Language :: Python :: 3.7+',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.7',
)