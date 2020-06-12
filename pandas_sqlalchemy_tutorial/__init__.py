"""Fetch and insert data into SQL database using Pandas."""
from config import (
	SQLALCHEMY_DATABASE_URI,
	SQLALCHEMY_ENGINE_OPTIONS,
	CSV_FILE
)
from .read import load_csv_data
from .database import Database


def init_script():
	"""Demonstrate Pandas' SQLAlchemy integration."""
	jobs_df = load_csv_data(CSV_FILE)
	db = Database(SQLALCHEMY_DATABASE_URI, SQLALCHEMY_ENGINE_OPTIONS)
	upload_result = db.upload_dataframe_to_sql(jobs_df, 'nyc_jobs')
	download_result = db.get_dataframe_from_sql('nyc_jobs')
	return upload_result, download_result
