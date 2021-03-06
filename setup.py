#!/usr/bin/env python
# coding=utf-8
from __future__ import unicode_literals, absolute_import, print_function, division

from sopel import __version__
import sys

try:
    from setuptools import setup
except ImportError:
    print(
        'You do not have setuptools, and can not install Sopel. The easiest '
        'way to fix this is to install pip by following the instructions at '
        'http://pip.readthedocs.org/en/latest/installing.html\n'
        'Alternately, you can run sopel without installing it by running '
        '"python sopel.py"',
        file=sys.stderr,
    )
    sys.exit(1)

if sys.version_info < (2, 7) or (
        sys.version_info[0] > 3 and sys.version_info < (3, 3)):
    # Maybe not the cleanest or best way to do this, but I'm tired of answering
    # this fucking question, and if you get here you should go RTGDMFM.
    raise ImportError('Sopel requires Python 2.7+ or 3.3+.')
if sys.version_info.major == 2:
    print('Warning: Python 2.x is near end of life. Sopel support at that point is TBD.', file=sys.stderr)


def read_reqs(path):
    with open(path, 'r') as fil:
        return list(fil.readlines())


requires = read_reqs('requirements.txt')
if sys.version_info[0] < 3:
    requires.append('backports.ssl_match_hostname')
dev_requires = requires + read_reqs('dev-requirements.txt')

classifiers = [
    'Development Status :: 5 - Production/Stable',
    'Intended Audience :: Developers',
    'Intended Audience :: System Administrators',
    'License :: Eiffel Forum License (EFL)',
    'License :: OSI Approved :: Eiffel Forum License',
    'Operating System :: POSIX :: Linux',
    'Programming Language :: Python :: 2.7',
    'Programming Language :: Python :: 3.3',
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
    'Programming Language :: Python :: 3.7',
    'Topic :: Communications :: Chat :: Internet Relay Chat',
]

setup(
    name='sopel',
    version=__version__,
    description='Simple and extendible IRC bot',
    author='Elsie Powell',
    author_email='powell.518@gmail.com',
    url='https://sopel.chat/',
    long_description=(
        "Sopel is a simple, extendible, easy-to-use IRC Utility bot, written "
        "in Python. It's designed to be easy to use, easy to run, and easy to "
        "make new features for."
    ),
    # Distutils is shit, and doesn't check if it's a list of basestring
    # but instead requires str.
    packages=[str('sopel'), str('sopel.modules'),
              str('sopel.cli'), str('sopel.config'), str('sopel.tools')],
    classifiers=classifiers,
    license='Eiffel Forum License, version 2',
    platforms='Linux x86, x86-64',
    install_requires=requires,
    extras_require={'dev': dev_requires},
    entry_points={
        'console_scripts': [
            'sopel = sopel.cli.run:main',
            'sopel-config = sopel.cli.config:main',
        ]
    },
)
