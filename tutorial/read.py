"""Load data from local CSV into Pandas DataFrame."""
import pandas as pd


def load_csv_data(csv):
    """Create DataFrame from local CSV."""
    jobs_df = pd.read_csv(csv)
    return jobs_df
