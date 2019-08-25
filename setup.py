import io
import os
import re

from setuptools import find_packages
from setuptools import setup


def read(filename):
    filename = os.path.join(os.path.dirname(__file__), filename)
    text_type = type(u"")
    with io.open(filename, mode="r", encoding='utf-8') as fd:
        return re.sub(text_type(r':[a-z]+:`~?(.*?)`'), text_type(r'``\1``'), fd.read())


setup(
    name="pybioutils",
    version="0.1.0",
    url="https://github.com/wayneidoyle/pybioutils",
    license='GNU General Public License Version 2',

    author="Wayne Doyle",
    author_email="",

    description="Functions for performing bioinformatics analyses",
    long_description=read("README.rst"),

    packages=find_packages(exclude=('tests',)),

    install_requires=['numpy>=1.17.0',
                      'pandas>=0.25.1',
                      'matplotlib>=3.1.1',
                      'matplotlib-venn>=0.11.5',
                      'pybedtools>=0.8.0',
                      ],

    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
    ],
)
