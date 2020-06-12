"""Database configuration."""
from os import environ, path
from dotenv import load_dotenv

basedir = path.abspath(path.dirname(__file__))
load_dotenv(path.join(basedir, '.env'))


SQLALCHEMY_DATABASE_URI = environ.get('SQLALCHEMY_DATABASE_URI')
SQLALCHEMY_ENGINE_OPTIONS = {'ssl': {'ca': './creds/ca-certificate.crt'}}
CSV_FILE = 'data/nyc-jobs.csv'
