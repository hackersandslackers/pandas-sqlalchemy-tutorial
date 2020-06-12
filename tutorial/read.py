"""Load data from local CSV into Pandas DataFrame."""
import pandas as pd


def load_csv_data(csv):
    """Create DataFrame and clean column names."""
    jobs_df = pd.read_csv(csv)
    new_columns = [column.replace(' ', '_').lower() for column in jobs_df]
    jobs_df.columns = new_columns
    return jobs_df
