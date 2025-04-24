import pandas as pd

def load_data(filepath='accident.csv'):
    """Load the accident data from CSV"""
    data = pd.read_csv(filepath)
    return data
