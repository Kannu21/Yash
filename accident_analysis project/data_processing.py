import pandas as pd

def clean_data(data):
    """Clean the data and create necessary transformations"""
    # Clean data by removing NaN values for speed
    clean_data = data.dropna(subset=['Speed_of_Impact']).copy()
    
    # Calculate speed ranges
    clean_data.loc[:, 'Speed_Range'] = pd.cut(clean_data['Speed_of_Impact'], 
                                     bins=[0, 30, 60, 90, 120],
                                     labels=['0-30', '31-60', '61-90', '91-120'])
    
    return clean_data

def prepare_numeric_data(data):
    """Create a copy of the data with numeric values only"""
    numeric_data = data.copy()
    
    # Convert categorical variables to numeric
    numeric_data['Gender'] = numeric_data['Gender'].map({'Male': 0, 'Female': 1})
    numeric_data['Helmet_Used'] = numeric_data['Helmet_Used'].map({'No': 0, 'Yes': 1})
    numeric_data['Seatbelt_Used'] = numeric_data['Seatbelt_Used'].map({'No': 0, 'Yes': 1})
    
    # Drop rows with missing values for correlation analysis
    numeric_data = numeric_data.dropna()
    
    return numeric_data
