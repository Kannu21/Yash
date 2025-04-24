import pandas as pd

# 5. Create a DataFrame with the given data
data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eve'],
    'Age': [25, 30, 35, 40, 28],
    'City': ['New York', 'San Francisco', 'Los Angeles', 'Chicago', 'Austin'],
    'Occupation': ['Data Analyst', 'Software Dev', 'Data Scientist', 'Manager', 'Developer']
}

df = pd.DataFrame(data)

# Display the original DataFrame
print("Original DataFrame:")
print(df)
print("\n")

# Select all rows where the 'City' is either 'New York' or 'Chicago' using boolean indexing
nyc_chicago = df[df['City'].isin(['New York', 'Chicago'])]
print("Rows where City is either 'New York' or 'Chicago':")
print(nyc_chicago)
print("\n")

# Select rows where 'Age' is >= 30 and 'Occupation' is 'Software Dev' using boolean indexing
age_30_software_dev = df[(df['Age'] >= 30) & (df['Occupation'] == 'Software Dev')]
print("Rows where Age is >= 30 and Occupation is 'Software Dev':")
print(age_30_software_dev)