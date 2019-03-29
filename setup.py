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
from setuptools import setup, find_packages
from setuptools.dist import Distribution
from setup_utility import BehaveTestCommand, CleanCommand, LicenseHeaderCommand
import os


class GradleDistribution(Distribution, object):

    def __init__(self, attrs):
        attrs['name'] = os.getenv('PYGRADLE_PROJECT_NAME')
        attrs['version'] = os.getenv('PYGRADLE_PROJECT_VERSION')

cmd_classes = {
    'license_headers': LicenseHeaderCommand,
    'behave_test': BehaveTestCommand,
}
if CleanCommand:
    cmd_classes['clean'] = CleanCommand

setup(
    name='algos',
    version='0.1',
    description='Algos - A collection of toy algos for machine learning',
    author='Jorge M. Faleiro Jr.',
    author_email='j@falei.ro',
    url='https://github.com/jfaleiro/algos',
    download_url='https://github.com/jfaleiro/quantlet/tarball/master',
    license="Affero GPL, see LICENSE for details",
    packages=find_packages(),
    cmdclass=cmd_classes,
    setup_requires=['setupext-janitor'],
#    install_requires=['matplotlib','numpy','pipe','scipy','ipython[all]','networkx','trellis'],
    tests_require=['nose', 'tox'],
    test_suite='nose.collector',
#    install_requires=['matplotlib','pandas','numpy','pipe','scipy','ipython[all]','pipe','networkx'],
    install_requires=['pandas>=0.13.1',
                      'ipython[all]>=3.1.0',
                      'pipe>=1.4.1',
                      'networkx>=1.9.1',
                      'seaborn>=0.5.1'],
    classifiers=[
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: GNU AFFERO GENERAL PUBLIC LICENSE",
        "Operating System :: OS Independent",
        "Topic :: Software Development",
        "Topic :: Software Development :: Libraries :: Python Modules"
        ]
)
    
