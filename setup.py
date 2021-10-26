# -*- coding: utf-8 -*-
"""
Created on Wed Nov 11 12:36:48 2020

@author: zamcr
"""

import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="frake",
    version="0.1.3",
    author="Luis E. Zambrano-Cruzatty",
    author_email="luis.zambranocruzatty@maine.edu",
    description="Visualizing tool for Anura3D results",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='https://github.com/luisez1988/FRAKE/archive/refs/tags/0.1.3.tar.gz',
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
