from distutils.core import setup
from setuptools import find_packages

setup(name='hu59vore',
version='0.1',
author='Shuvanon Razik',
author_email='shuvanon.razik@fau.de',
packages=find_packages(),
install_requires=['numpy', 'Pillow', 'ipywidgets'])