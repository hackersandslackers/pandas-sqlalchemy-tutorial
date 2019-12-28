"""A setuptools based setup module."""
from os import path
from setuptools import setup, find_packages
from io import open

here = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='Pandas SQLAlchemy Tutorial',
    version='0.0.1',
    description='Easily drop data into Pandas from a SQL database or upload DataFrames to a SQL table.',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/hackersandslackers/pandas-sqlalchemy-tutorial',
    author='Todd Birchard',
    author_email='hackersandslackers@gmail.com',
    classifiers=[
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.7',
    ],
    keywords='Flask Flask-WTF Forms',
    packages=find_packages(),
    install_requires=['Pandas',
                      'SQLAlchemy',
                      'Psycopg2-binary'],
    extras_require={
        'dev': ['check-manifest'],
        'test': ['coverage'],
        'env': ['python-dotenv']
    },
    entry_points={
        'console_scripts': [
            'install=wsgi:__main__',
        ],
    },
    project_urls={
        'Bug Reports': 'https://github.com/hackersandslackers/pandas-sqlalchemy-tutorial/issues',
        'Source': 'https://github.com/hackersandslackers/pandas-sqlalchemy-tutorial/',
    },
)
