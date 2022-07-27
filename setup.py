#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

setup(
    name="inginious-problems-math",
    version="0.1dev1",
    description="Plugin to add math formulas problem type",
    packages=find_packages(),
    install_requires=["inginious>=0.5.dev0", "sympy", "antlr4-python3-runtime==4.9.3"],
    tests_require=[],
    extras_require={},
    scripts=[],
    include_package_data=True,
    author="The INGInious authors",
    author_email="inginious@info.ucl.ac.be",
    license="AGPL 3",
    url="https://github.com/UCL-INGI/INGInious-problems-math"
)
