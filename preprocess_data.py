import pandas as pd

# Load data into pandas DataFrames
artists_df = pd.read_csv("artists.csv")
albums_df = pd.read_csv("albums.csv")
tracks_df = pd.read_csv("tracks.csv")

# Define columns to remove for each DataFrame
artists_columns_to_remove = ['genre']
albums_columns_to_remove = ['track_number', 'album_type', 'artists', 'total_tracks']
tracks_columns_to_remove = ['track_popularity']

# Remove specified columns from each DataFrame
artists_df.drop(columns=artists_columns_to_remove, inplace=True)
albums_df.drop(columns=albums_columns_to_remove, inplace=True)
tracks_df.drop(columns=tracks_columns_to_remove, inplace=True)

# Remove null values from each DataFrame
artists_df.dropna(inplace=True)
albums_df.dropna(inplace=True)
tracks_df.dropna(inplace=True)

# Save the preprocessed DataFrames to CSV files
artists_df.to_csv("artists.csv", index=False)
albums_df.to_csv("albums.csv", index=False)
tracks_df.to_csv("tracks.csv", index=False)
