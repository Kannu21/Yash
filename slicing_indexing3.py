import pandas as pd

# 3. Create a DataFrame with the given data
data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David'],
    'Age': [25, 30, 35, 40],
    'City': ['New York', 'San Francisco', 'Los Angeles', 'Chicago'],
    'Occupation': ['Data Analyst', 'Software Dev', 'Data Scientist', 'Manager']
}

df = pd.DataFrame(data)

# Display the DataFrame
print("Original DataFrame:")
print(df)
print("\n")

# Access the 'Occupation' of David using label-based indexing
david_occupation = df.loc[df['Name'] == 'David', 'Occupation'].values[0]
print("Occupation of David using label-based indexing:")
print(david_occupation)
print("\n")

# Access the 'Age' of Charlie using position-based indexing
charlie_age = df.loc[df['Name'] == 'Charlie', 'Age'].values[0]
print("Age of Charlie using position-based indexing:")
print(charlie_age)
print("\n")

# Access the element at row 2 (Charlie) and column 2 (City) using position-based indexing
# Note: Using zero-based indexing, row 2 refers to the 3rd row (Charlie)
# and column 2 refers to the 3rd column (City)
charlie_city = df.iloc[2, 2]
print("Element at row 2 (Charlie) and column 2 (City) using position-based indexing:")
print(charlie_city)