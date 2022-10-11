from setuptools import setup, find_packages
import codecs
import os

here = os.path.abspath(os.path.dirname(__file__))

with codecs.open(os.path.join(here, "README.md"), encoding="utf-8") as fh:
    long_description = "\n" + fh.read()

VERSION = '0.0.1'
DESCRIPTION = 'A package that types for you'
LONG_DESCRIPTION = 'A quick and small python package that helps you autotype on websites that have copy paste disabled.'

# Setting up
setup(
    name="autotype",
    version=VERSION,
    author="Tushar Gupta (tushar5526)",
    author_email="<tushar.gupta5526@gmail.com>",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=long_description,
    packages=find_packages(),
    install_requires=['pynput==1.7.3',
    'python-xlib==0.30',
    'six==1.16.0',
    "pyobjc==7.1; sys_platform=='darwin'",
    'tk==0.1.0',
    'pillow==9.1.1',
    'typer==0.4.2'
    ],
    keywords=['autotype','auto','type'],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)