# Pandas SQLAlchemy Tutorial

![Python](https://img.shields.io/badge/Python-v^3.8-blue.svg?logo=python&longCache=true&logoColor=white&colorB=5e81ac&style=flat-square&colorA=4c566a)
![Pandas](https://img.shields.io/badge/Pandas-v^1.0.0-blue.svg?logo=python&longCache=true&logoColor=white&colorB=5e81ac&style=flat-square&colorA=4c566a)
![SQLAlchemy](https://img.shields.io/badge/SQLAlchemy-^1.3.6-red.svg?longCache=true&style=flat-square&logo=python&logoColor=white&colorA=4c566a&colorB=bf616a)
![PyMySQL](https://img.shields.io/badge/PyMySQL-v0.9.3-red.svg?longCache=true&style=flat-square&logo=mysql&logoColor=white&colorA=4c566a&colorB=bf616a)
![GitHub Last Commit](https://img.shields.io/github/last-commit/google/skia.svg?style=flat-square&colorA=4c566a&colorB=a3be8c)
[![GitHub Issues](https://img.shields.io/github/issues/hackersandslackers/pandas-sqlalchemy-tutorial.svg?style=flat-square&colorA=4c566a&colorB=ebcb8b)](https://github.com/hackersandslackers/pandas-sqlalchemy-tutorial/issues)
[![GitHub Stars](https://img.shields.io/github/stars/hackersandslackers/pandas-sqlalchemy-tutorial.svg?style=flat-square&colorB=ebcb8b&colorA=4c566a)](https://github.com/hackersandslackers/pandas-sqlalchemy-tutorial/stargazers)
[![GitHub Forks](https://img.shields.io/github/forks/hackersandslackers/pandas-sqlalchemy-tutorial.svg?style=flat-square&colorA=4c566a&colorB=ebcb8b)](https://github.com/hackersandslackers/pandas-sqlalchemy-tutorial/network)

![Pandas SQLAlchemy Tutorial](https://github.com/hackersandslackers/pandas-sqlalchemy-tutorial/blob/master/.github/pandas-sqlalchemy@2x.jpg?raw=true)

Easily drop data into Pandas from a SQL database, or upload your DataFrames to a SQL table. Tutorial found here: https://hackersandslackers.com/connecting-pandas-to-a-sql-database-with-sqlalchemy/


## Installation

**Installation via `requirements.txt`**:

```shell
$ git clone https://github.com/hackersandslackers/pandas-sqlalchemy-tutorial.git
$ cd pandas-sqlalchemy-tutorial
$ python3 -m venv myenv
$ source myenv/bin/activate
$ pip3 install -r requirements.txt
$ python3 main.py
```

**Installation via [Pipenv](https://pipenv-fork.readthedocs.io/en/latest/)**:

```shell
$ git clone https://github.com/hackersandslackers/pandas-sqlalchemy-tutorial.git
$ cd pandas-sqlalchemy-tutorial
$ pipenv shell
$ pipenv update
$ python3 main.py
```

**Installation via [Poetry](https://python-poetry.org/)**:

```shell
$ git clone https://github.com/hackersandslackers/pandas-sqlalchemy-tutorial.git
$ cd pandas-sqlalchemy-tutorial
$ poetry shell
$ poetry update
$ poetry run
```

## Usage

Replace the values in **.env.example** with your values and rename this file to **.env**:

* `SQLALCHEMY_DATABASE_URI`: Connection URI of a SQL database.

*Remember never to commit secrets saved in .env files to Github.*

------------------

**Hackers and Slackers** tutorials are free of charge. If you found this tutorial helpful, a [small donation](https://www.buymeacoffee.com/hackersslackers) would be greatly appreciated to keep us in business. All proceeds go towards coffee, and all coffee goes towards more content.
