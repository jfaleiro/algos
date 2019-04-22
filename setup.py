#!/usr/bin/env python
#
#      Algos - A collection of toy algos for machine learning.
#
#      Copyright (C) 2019 Jorge M. Faleiro Jr.
#
#      This program is free software: you can redistribute it and/or modify
#      it under the terms of the GNU Affero General Public License as published
#      by the Free Software Foundation, either version 3 of the License, or
#      (at your option) any later version.
#
#      This program is distributed in the hope that it will be useful,
#      but WITHOUT ANY WARRANTY; without even the implied warranty of
#      MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#      GNU Affero General Public License for more details.
#
#      You should have received a copy of the GNU Affero General Public License
#      along with this program.  If not, see <http://www.gnu.org/licenses/>.
#

try:
    import setup_utility
except ModuleNotFoundError as e:
    from pip._internal import main
    assert main('install jfaleiro.setup_utility'.split()) == 0

import pathlib

from setuptools import setup, find_packages


from setup_utility import (
    BehaveTestCommand,
    CleanCommand,
    LicenseHeaderCommand,
    ToxCommand,
    version_from_git,
)


setup(
    name='jfaleiro.algos',
    version=version_from_git(),
    description='Algos - A collection of toy algos for machine learning',
    long_description=(pathlib.Path(__file__).parent / 'README.md').read_text(),
    long_description_content_type='text/markdown',
    author='Jorge M. Faleiro Jr.',
    author_email='j@falei.ro',
    url='https://github.com/jfaleiro/algos',
    license="Affero GPL, see LICENSE for details",
    packages=find_packages(),
    cmdclass={
        'behave_test': BehaveTestCommand,
        'clean': CleanCommand,
        'license_headers': LicenseHeaderCommand,
        'tox': ToxCommand,
    },
    setup_requires=[
        'twine',
        'wheel',
        'setuptools>=38.6.0',
        'jfaleiro.setup_utility',
        'setupext-janitor',
        'behave',
        'nose>=1.0'
    ],
    tests_require=[
        'pytest',
        'pytest-cov',
        'PyHamCrest',
    ],
    test_suite='nose.collector',
    install_requires=[
        'setuptools>=38.6.0',
        'jfaleiro.setup_utility',
        'pandas>=0.24.2',
    ],
    classifiers=[
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: GNU Affero General Public License v3",
        "Operating System :: OS Independent",
        "Topic :: Software Development",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ]
)
