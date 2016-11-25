#! /usr/bin/env python

# Copyright (C) 2001-2003 Michael Haggerty <mhagger@alum.mit.edu>
#
# This file is licensed under the GNU Lesser General Public License
# (LGPL).  See LICENSE.txt for details.

"""Setup script for the Gnuplot module distribution.

"""

from setuptools import setup, find_packages

long_description = """\
Gnuplot.py is a Python package that allows you to create graphs from
within Python using the gnuplot plotting program.
"""

setup (
      # Distribution meta-data
      name='gnuplot-py',
      version='1.8',
      description='A Python interface to the gnuplot plotting program.',
      long_description=long_description,
      author='Michael Haggerty',
      author_email='mhagger@alum.mit.edu',
      url='http://gnuplot-py.sourceforge.net',
      license='LGPL',
      # Description of the package in the distribution
      package_dir={'Gnuplot' : '.'},
      #packages=['Gnuplot'],
      packages = ['gnuplot'],
     )

