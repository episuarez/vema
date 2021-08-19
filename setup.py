from os import path

from setuptools import find_packages, setup

this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, "readme.md"), encoding="utf-8") as file:
    long_description = file.read()

setup(
    name="vema",
    version="0.1.3",
    description="Vema is a solution for developing static web pages, from Python + Flask, which has the basic tools and already configured to focus on the design of the pages.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    license="MIT",
    author="Epifanio Suárez Martínez",
    author_email="episuarez@pm.es",
    url="https://github.com/episuarez/vema",
    packages=["vema", "vema/src", "vema/src/exceptions"],
    install_requires=["Flask", "Frozen-Flask", "argparse"],
    setup_requires=['pytest-runner'],
    tests_require=['pytest'],
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
    ]
);
