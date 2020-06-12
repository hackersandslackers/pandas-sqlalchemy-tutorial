"""Fetch and insert data into SQL database using Pandas."""
from .read import load_csv_data
from .database import Database
from config import (
	SQLALCHEMY_DATABASE_URI,
	SQLALCHEMY_ENGINE_OPTIONS,
	CSV_FILE
)


def init_script():
	"""Demonstrate Pandas' SQLAlchemy integration."""
	jobs_df = load_csv_data(CSV_FILE)
	db = Database(SQLALCHEMY_DATABASE_URI, SQLALCHEMY_ENGINE_OPTIONS)
	db.upload_dataframe_to_sql(jobs_df, 'nyc_jobs')
	db.get_dataframe_from_sql('nyc_jobs')
