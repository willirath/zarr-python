# -*- coding: utf-8 -*-
import sys

from setuptools import setup

DESCRIPTION = 'An implementation of chunked, compressed, ' \
              'N-dimensional arrays for Python.'

with open('README.rst') as f:
    LONG_DESCRIPTION = f.read()

dependencies = [
    'asciitree',
    'numpy>=1.7',
    'fasteners',
    'numcodecs>=0.6.2',
]

setup(
    name='zarr',
    description=DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    use_scm_version={
        'version_scheme': 'guess-next-dev',
        'local_scheme': 'dirty-tag',
        'write_to': 'zarr/version.py'
    },
    setup_requires=[
        'setuptools>18.0',
        'setuptools-scm>1.5.4'
    ],
    python_requires='>=3.5',
    install_requires=dependencies,
    package_dir={'': '.'},
    packages=['zarr', 'zarr.tests'],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Intended Audience :: Information Technology',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Operating System :: Unix',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
    ],
    maintainer='Alistair Miles',
    maintainer_email='alimanfoo@googlemail.com',
    url='https://github.com/zarr-developers/zarr-python',
    license='MIT',
)
