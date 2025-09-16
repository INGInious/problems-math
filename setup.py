#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

doc_requires = [
    "ipython==8.12.3",
    "sphinx==7.4.7",
    "sphinx-autodoc-typehints==2.3.0",
    "sphinx-rtd-theme==3.0.0",
    "sphinx-tabs==3.4.5"
]


setup(
    name="inginious-problems-math",
    version="0.1dev1",
    description="Plugin to add math formulas problem type",
    packages=find_packages(),
    install_requires=["inginious", "sympy==1.13.3", "antlr4-python3-runtime==4.11.1"],
    tests_require=[],
    extras_require={"doc": doc_requires},
    scripts=[],
    include_package_data=True,
    author="The INGInious authors",
    author_email="inginious@info.ucl.ac.be",
    license="AGPL 3",
    url="https://github.com/UCL-INGI/INGInious-problems-math"
)
