#!/usr/bin/env python

from setuptools import setup

setup(name='PyDirectoryCleanup',
      version='1.0',
      author='Clark Stoner',
      author_email='clark@clarkstoner.com',
      packages=['PyDirectoryCleanup',
                'PyDirectoryCleanup.src'],
      install_requires=['watchdog'],
      scripts=['PyDirectoryCleanup/bin/config_generator.py'],
      description='A simple program to keep a directory clean on your machine using Python and Watchdog',
      long_description=open('README.txt').read(),
      )