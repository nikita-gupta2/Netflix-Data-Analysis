import pandas as pd
from collections import Counter

# -------------------------------------------------
# LOAD DATA
# -------------------------------------------------
def load_data(path):
    """
    Load the Netflix dataset from a CSV file.
    """
    return pd.read_csv(path)


# -------------------------------------------------
# DATA CLEANING
# -------------------------------------------------
def clean_missing_values(df):
    """
    Fill missing values for key columns.
    """
    df['country'].fillna('Unknown', inplace=True)
    df['cast'].fillna('Not Specified', inplace=True)
    df['director'].fillna('Not Specified', inplace=True)
    df['rating'].fillna('Not Rated', inplace=True)

    # Drop rows where date_added is missing
    df.dropna(subset=['date_added'], inplace=True)
    return df


# -------------------------------------------------
# GENRE PROCESSING
# -------------------------------------------------
def get_top_genres(df, n=10):
    """
    Split 'listed_in' column (genres) and return top n genres.
    """
    genres = df['listed_in'].dropna().apply(lambda x: x.split(', '))
    flat_genres = [genre for sublist in genres for genre in sublist]
    return pd.Series(flat_genres).value_counts().head(n)


# -------------------------------------------------
# DATE PROCESSING
# -------------------------------------------------
def extract_year(df):
    """
    Convert 'date_added' to datetime and extract the year.
    """
    df['year_added'] = pd.to_datetime(
        df['date_added'].str.strip(),
        errors='coerce',
        infer_datetime_format=True
    ).dt.year
    return df


# -------------------------------------------------
# SAVE CLEANED DATA
# -------------------------------------------------
def save_cleaned_data(df, path):
    """
    Save cleaned DataFrame to CSV.
    """
    df.to_csv(path, index=False)
    return True
