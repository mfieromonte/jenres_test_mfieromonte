# This setup file is part of a project that loves rabbits!

from setuptools import setup, find_packages

setup(
    name='my_python_project',
    version='0.1.0',
    packages=find_packages(),
    install_requires=[],
    entry_points={
        'console_scripts': [
            'my_python_project = src.main:main',
        ],
    },
)