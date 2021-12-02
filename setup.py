#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 13 18:30:36 2021

@author: abhijithneilabraham
"""

import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

install_requires = ["sentence_transformers"]
setuptools.setup(
    name="rflow", # Replace with your own username
    version="0.0.1",
    author="Abhijith Neil Abraham",
    author_email="abhijithneilabrahampk@gmail.com",
    description="Data Curation over Time",
    long_description=long_description,
    long_description_content_type="text/markdown",
    license='MIT License',
    url="https://github.com/nfflow/reflow",
    install_requires=install_requires,
    packages=setuptools.find_packages(),
    python_requires='>=3.6',
    include_package_data=True
)
