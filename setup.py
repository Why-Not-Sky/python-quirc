# -*- coding: utf-8 -*-

"""
python-quirc
============

python-quirc is a ctypes bindings for `quirc <https://github.com/dlbeer/quirc/>`_, library for decoding QR codes.

This library is fast, small, easy to use, have a very small memory usage,
and optionally requires one of the image processing libraries.
"""

from setuptools import setup

setup(
    name='quirc',
    version='0.6.2',
    author='SvartalF',
    author_email='self@svartalf.info',
    url='https://github.com/svartalf/python-quirc',
    description='ctypes wrapper for QR code decoding library `libquirc`',
    long_description=__doc__,
    packages=('quirc',),
    test_suite='tests.load_tests',
    classifiers=(
        'Development Status :: 1 - Planning',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.5',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: Implementation :: PyPy',
        'Topic :: Software Development :: Libraries',
        'Topic :: Scientific/Engineering :: Image Recognition',
        'Topic :: Multimedia :: Graphics',
    ),
)
