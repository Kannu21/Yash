import pandas as pd
import numpy as np

# Task 1: Create a DataFrame with custom index from 10, incrementing by 2
def create_custom_indexed_df():
    """Create a DataFrame with a custom index starting at 10, incrementing by 2"""
    # Sample data
    data = {
        'Product': ['Laptop', 'Smartphone', 'Tablet', 'Headphones', 'Monitor'],
        'Price': [1200, 800, 500, 150, 350],
        'Stock': [10, 25, 15, 30, 8]
    }
    
    # Create DataFrame
    df = pd.DataFrame(data)
    
    # Create custom index
    df.index = range(10, 10 + 2*len(df), 2)
    
    # Access second row (index 12)
    second_row = df.loc[12]
    
    return df, second_row

# Task 2: Rename the Name index to "Person"
def rename_name_index_to_person():
    """Convert Name column to index and rename it to 'Person'"""
    data = {
        'Name': ['John', 'Emma', 'Raj', 'Sofia', 'Miguel'],
        'Department': ['Sales', 'IT', 'Finance', 'HR', 'Marketing'],
        'Salary': [65000, 85000, 70000, 68000, 72000]
    }
    
    # Create DataFrame with Name as index
    df = pd.DataFrame(data).set_index('Name')
    
    # Rename the index
    df.index.name = 'Person'
    
    return df

# Task 3: Change specific index label from Ashish to Ankit
def change_index_label():
    """Change a specific index label in a DataFrame"""
    # Create DataFrame with Name index already set
    data = {
        'Project': ['Alpha', 'Beta', 'Gamma', 'Delta'],
        'Budget': [50000, 75000, 60000, 90000],
        'Team Size': [5, 8, 6, 10]
    }
    
    # Create DataFrame with custom index
    index_labels = ['Ashish', 'Priya', 'Michael', 'Sara']
    df = pd.DataFrame(data, index=index_labels)
    df.index.name = 'Name'
    
    # Change index label
    df = df.rename(index={'Ashish': 'Ankit'})
    
    return df

# Task 4: Reindex DataFrame with custom labels
def reindex_with_custom_labels():
    """Reindex a DataFrame with custom labels"""
    data = {
        'Country': ['USA', 'India', 'Brazil', 'Japan'],
        'Population': [331, 1380, 212, 126],  # millions
        'Area': [9834, 3287, 8516, 378]  # thousands of sq km
    }
    
    df = pd.DataFrame(data)
    
    # Reindex with custom labels
    new_labels = ['a', 'b', 'c', 'd']
    df_reindexed = df.reindex(index=new_labels)
    
    return df_reindexed

# Task 5: Reset index and move it back to regular column
def reset_name_index():
    """Reset index that was a Name column and convert back to regular column"""
    data = {
        'Age': [28, 34, 42, 25, 39],
        'City': ['Boston', 'Chicago', 'Seattle', 'Miami', 'Denver']
    }
    
    # Create DataFrame with names as index
    names = ['Alex', 'Tina', 'Carlos', 'Priya', 'Jackson']
    df = pd.DataFrame(data, index=names)
    df.index.name = 'Name'
    
    # Reset index to move it back as a column
    df_reset = df.reset_index()
    
    return df_reset

# Task 6: Access age of specific person by index
def access_person_by_name_index():
    """Create a DataFrame with Name as index and access specific person's data"""
    data = {
        'Name': ['John', 'Sara', 'Amit', 'Maria', 'Chen'],
        'Age': [32, 28, 45, 39, 27],
        'City': ['New York', 'London', 'Mumbai', 'Madrid', 'Beijing']
    }
    
    # Create DataFrame and set Name as index
    df = pd.DataFrame(data).set_index('Name')
    
    # Access Amit's age
    amit_age = df.loc['Amit', 'Age']
    
    return df, amit_age

# Task 7: Load and modify Titanic dataset
def process_titanic_dataset():
    """Load Titanic dataset and rename columns"""
    # Create a sample Titanic dataset for demonstration
    titanic = pd.DataFrame({
        'PassengerId': list(range(1, 6)),
        'Survived': [0, 1, 1, 0, 1],
        'Pclass': [3, 1, 2, 3, 1],
        'Name': ['Braund, Mr. Owen Harris', 
                'Cumings, Mrs. John Bradley',
                'Heikkinen, Miss. Laina',
                'Allen, Mr. William Henry',
                'Moran, Mr. James'],
        'Sex': ['male', 'female', 'female', 'male', 'male'],
        'Age': [22, 38, 26, 35, 27],
        'Fare': [7.25, 71.28, 7.92, 8.05, 8.46]
    })
    
    # Display original column names
    original_columns = titanic.columns.tolist()
    
    # Rename columns
    renamed_titanic = titanic.rename(columns={
        'Name': 'PassengerName',
        'Pclass': 'PassengerClass'
    })
    
    return renamed_titanic, original_columns