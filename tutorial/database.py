"""Interact with SQL database via Pandas & SQLAlchemy."""
from sqlalchemy import create_engine
from sqlalchemy.types import Integer, Text, String, DateTime
import pandas as pd


class Database:

    def __init__(self, db_uri, db_args):
        self.engine = create_engine(
            db_uri,
            connect_args=db_args,
            echo=True
        )

    def upload_dataframe_to_sql(self, local_df):
        """Upload data to database with proper dtypes."""
        local_df.to_sql(
            "nyc_jobs",
            self.engine,
            if_exists='append',
            index=False,
            chunksize=500,
            dtype={
                "job_id": Integer,
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
                "posting_updated": DateTime
            }
        )

    def get_dataframe_from_sql(self, table_name):
        """Create DataFrame form SQL table."""
        sql_DF = pd.read_sql_table(
            table_name,
            con=self.engine,
            parse_dates=['posting_date', 'posting_updated']
        )
        return sql_DF

