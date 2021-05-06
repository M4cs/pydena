#!/usr/bin/env python3

import sys, requests
from setuptools import setup, find_packages

setup(
    name='pydena',
    version='1.0.0',
    author='Max Bridgland',
    author_email='me@maxbridgland.com',
    description='Unofficial idena-go RPC API Python Wrapper',
    long_description=open('README.md', 'r', encoding='utf-8').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/M4cs/BabySploit',
    packages=find_packages(include=['pydena','pydena.*']),
    install_requires=[
        'requests',
        'pydantic'
    ],
    project_urls={
        'Wiki': 'https://github.com/M4cs/pydena',
        'Discord Server': 'https://discord.gg/hRxhMGtMed'
    },
    license='GNU General Public License v3 (GPLv3) (GPL)',
    zip_safe=True,
    tests_require=[
        'mock;python_version<"3.6"',
        'pytest',
        'pytest-cov'
    ],
    classifiers=[  # Used by PyPI to classify the project and make it searchable
        'Development Status :: 4 - Beta',
        'Environment :: Console',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',

        'Programming Language :: Python',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: Implementation :: PyPy',
        'Programming Language :: Python :: Implementation :: IronPython',
        'Programming Language :: Python :: Implementation :: Jython',

        'Intended Audience :: Developers',
        'Intended Audience :: System Administrators',
        'Intended Audience :: Information Technology',

        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Software Development :: Libraries',
        'Topic :: System :: Systems Administration',
        'Topic :: System :: Networking',
        'Topic :: Utilities',
    ]
)
