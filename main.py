from os import environ
from sqlalchemy import create_engine
from sqlalchemy.types import Integer, Text, String, DateTime
import pandas as pd


db_URI = environ.get('SQLALCHEMY_DATABASE_URI')
db_schema = environ.get('SQLALCHEMY_DB_SCHEMA')
engine = create_engine(db_URI,
                       connect_args={'sslmode': 'require'},
                       echo=True)


def prepare_data():
    """Create DataFrame and clean column names."""
    jobs_DF = pd.read_csv('data/nyc-jobs.csv')
    new_columns = [column.replace(' ', '_').lower() for column in jobs_DF]
    jobs_DF.columns = new_columns
    return jobs_DF


def upload_dataframe_to_sql(jobs_DF):
    """Upload data to db with proper dtypes."""
    jobs_DF.to_sql("nyc_jobs",
                   engine,
                   if_exists='append',
                   schema=db_schema,
                   index=False,
                   chunksize=500,
                   dtype={"job_id": Integer,
                          "agency": Text,
                          "business_title": Text,
                          "job_category":  Text,
                          "salary_range_from": Integer,
                          "salary_range_to": Integer,
                          "salary_frequency": String(50),
                          "work_location": Text,
                          "division/work_unit": Text,
                          "job_description": Text,
                          "posting_date": DateTime,
                          "posting_updated": DateTime})


def get_dataframe_from_sql(table_name):
    """Create DataFrame form SQL table."""
    sql_DF = pd.read_sql_table(table_name,
                               con=engine,
                               parse_dates=['posting_date', 'posting_updated'])
    return sql_DF


jobs_DF = prepare_data()
print(jobs_DF.info())
upload_dataframe_to_sql(jobs_DF)
get_dataframe_from_sql('nyc_jobs')
