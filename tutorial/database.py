"""Interact with SQL database via Pandas & SQLAlchemy."""
from sqlalchemy import create_engine
from sqlalchemy.types import Integer, Text, String, DateTime
import pandas as pd


class Database:
    """Pandas database client."""

    def __init__(self, db_uri, db_args):
        self.engine = create_engine(
            db_uri,
            connect_args=db_args,
            echo=True
        )

    def upload_dataframe_to_sql(self, csv_df, table_name):
        """Upload data to database with proper dtypes."""
        csv_df.to_sql(
            table_name,
            self.engine,
            if_exists='replace',
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
        print(f'Loaded {len(csv_df)} rows into {table_name} table.')

    def get_dataframe_from_sql(self, table_name):
        """Create DataFrame form SQL table."""
        table_df = pd.read_sql_table(
            table_name,
            con=self.engine
        )
        print(f'Loaded {len(table_df)} rows from {table_name}.')
        print(table_df.info())
        return table_df

