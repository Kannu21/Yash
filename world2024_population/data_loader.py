import pandas as pd
import numpy as np

def load_population_data(file_path='test.csv'):
    """Load the population data from a CSV file."""
    df = pd.read_csv(file_path)
    return df

def clean_data(df):
    """Clean and prepare the population data."""
    # Convert string numbers with commas to float
    for col in ['Population (2024)', 'Net Change', 'Land Area (Km²)', 'Migrants (net)', 'Density (P/Km²)']:
        df[col] = df[col].str.replace(',', '').astype(float)
    
    # Convert percentages to float
    for col in ['Yearly Change', 'World Share']:
        df[col] = df[col].str.rstrip(' %').astype(float) / 100
    
    # Handle special cases like "N.A." in Urban Pop %
    df['Urban Pop %'] = df['Urban Pop %'].replace('N.A.', np.nan)
    df['Urban Pop %'] = df['Urban Pop %'].str.rstrip(' %').astype(float) / 100
    
    return df